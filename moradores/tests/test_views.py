import responses
import json

from django.test import TestCase
from django.urls import reverse
from faker import Faker
from urllib.parse import urlencode

from moradores.models import Bairro
from moradores.models import Morador


class MoradoresListaViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/moradores/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('moradores_lista'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('moradores_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_lista.html')


class ExcluirMoradorViewTest(TestCase):
    def setUp(self):
        faker = Faker(["pt_BR"])

        bairro = Bairro.objects.create(
            bairro=faker.bairro(),
            cep=faker.postcode(),
            logradouro=faker.street_name(),
        )

        self.morador = Morador.objects.create(
            nome=faker.name(),
            cep=faker.postcode(),
            endereco=faker.street_name(),
            numero_endereco=faker.building_number(),
            bairro=bairro,
            whatsapp=faker.cellphone_number,
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post(
            f'/moradores/excluir_morador/{self.morador.pk}/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.post(
            reverse('excluir_morador', args=[self.morador.pk]), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_redirect_to_the_correct_template(self):
        response = self.client.post(
            reverse('excluir_morador', args=[self.morador.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_lista.html')


class MoradoresEdicaoViewTest(TestCase):
    def setUp(self):
        self.faker = Faker(["pt_BR"])

        cep = self.faker.postcode()

        bairro = Bairro.objects.create(
            bairro=self.faker.bairro(),
            cep=cep,
            logradouro=self.faker.street_name(),
        )

        self.morador = Morador.objects.create(
            nome=self.faker.name(),
            cep=cep,
            endereco=self.faker.street_name(),
            numero_endereco=self.faker.building_number(),
            bairro=bairro,
            whatsapp=self.faker.cellphone_number(),
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/moradores/editar/{self.morador.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse('moradores_edicao', args=[self.morador.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse('moradores_edicao', args=[self.morador.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_edicao.html')

    @responses.activate
    def test_view_edits_morador_properly(self):
        responses.add(responses.GET, f'https://viacep.com.br/ws/{self.morador.cep}/json/',
                      body=json.dumps({'bairro': 'foo', 'logradouro': 'baz'}), status=200, content_type="application/json")

        data = {'nome': self.morador.nome,
                'cep': self.morador.cep,
                'endereco': self.morador.endereco,
                'numero_endereco': self.morador.numero_endereco,
                'bairro': self.morador.bairro,
                'whatsapp': self.faker.cellphone_number()}

        response = self.client.post(reverse('moradores_edicao', args=[
                                    self.morador.pk]),  data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_lista.html')

        responses.reset()

    @responses.activate
    def test_view_creates_new_bairro_if_cep_doesnt_exists_in_database(self):
        new_cep = self.faker.postcode()

        responses.add(responses.GET, f'https://viacep.com.br/ws/{new_cep}/json/',
                      body=json.dumps({'bairro': 'foo', 'logradouro': 'bar'}), status=200, content_type="application/json")

        data = {'nome': self.morador.nome,
                'cep': new_cep,
                'endereco': self.morador.endereco,
                'numero_endereco': self.morador.numero_endereco,
                'bairro': self.morador.bairro,
                'whatsapp': self.morador.whatsapp}

        response = self.client.post(reverse('moradores_edicao', args=[
                                    self.morador.pk]),  data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_lista.html')

        new_bairro = Bairro.objects.get(pk=2)
        self.assertEqual(new_bairro.bairro, 'foo')
        self.assertEqual(new_bairro.logradouro, 'bar')

        responses.reset()

    def test_view_warns_user_that_cep_is_invalid(self):
        new_cep = self.faker.postcode()

        responses.add(responses.GET, f'https://viacep.com.br/ws/{new_cep}/json/',
                      body={json.dumps({'erro': True})}, status=200, content_type="application/json")

        data = {'nome': self.morador.nome,
                'cep': new_cep,
                'endereco': self.morador.endereco,
                'numero_endereco': self.morador.numero_endereco,
                'bairro': self.morador.bairro,
                'whatsapp': self.morador.whatsapp}

        response = self.client.post(reverse('moradores_edicao', args=[
                                    self.morador.pk]),  data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_edicao.html')
        self.assertEqual(
            response.context['erro'], 'Você digitou um CEP invalido. Tente novamente.')

        responses.reset()


class MoradoresFormularioViewTest(TestCase):
    def setUp(self):
        self.faker = Faker(["pt_BR"])

        cep = self.faker.postcode()

        self.bairro = Bairro.objects.create(
            bairro=self.faker.bairro(),
            cep=cep,
            logradouro=self.faker.street_name(),
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/moradores/formulario/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse('moradores_formulario'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse('moradores_formulario'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_formulario.html')

    @responses.activate
    def test_view_creates_morador_properly(self):
        morador = {
            'nome': self.faker.name(),
            'cep': self.bairro.cep,
            'endereco': self.faker.street_name(),
            'numero_endereco': self.faker.building_number(),
            'bairro': self.bairro.bairro,
            'whatsapp': self.faker.cellphone_number()
        }
        responses.add(responses.GET, f'https://viacep.com.br/ws/{self.bairro.cep}/json/',
                      body=json.dumps({'bairro': 'foo', 'logradouro': 'baz'}), status=200, content_type="application/json")

        response = self.client.post(
            reverse('moradores_formulario'),  data=morador, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_lista.html')

        expectedMorador = Morador.objects.get(pk=1)
        self.assertEqual(expectedMorador.nome, morador['nome'].capitalize())

        responses.reset()

    @responses.activate
    def test_view_creates_morador_and_bairro_if_cep_doesnt_exists_in_database(self):
        cep = self.faker.postcode()
        morador = {
            'nome': self.faker.name(),
            'cep': cep,
            'endereco': self.faker.street_name(),
            'numero_endereco': self.faker.building_number(),
            'bairro': self.faker.bairro(),
            'whatsapp': self.faker.cellphone_number()
        }
        responses.add(responses.GET, f'https://viacep.com.br/ws/{cep}/json/',
                      body=json.dumps({'bairro': 'foo', 'logradouro': 'baz'}), status=200, content_type="application/json")

        response = self.client.post(
            reverse('moradores_formulario'),  data=morador, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_lista.html')

        expectedMorador = Morador.objects.get(pk=1)
        self.assertEqual(expectedMorador.nome, morador['nome'].capitalize())

        expectedBairro = Bairro.objects.get(pk=2)
        self.assertEqual(expectedBairro.bairro, 'foo')

        responses.reset()

    def test_view_warns_user_that_cep_is_invalid(self):
        cep = self.faker.postcode()
        morador = {
            'nome': self.faker.name(),
            'cep': cep,
            'endereco': self.faker.street_name(),
            'numero_endereco': self.faker.building_number(),
            'bairro': self.faker.bairro(),
            'whatsapp': self.faker.cellphone_number()
        }
        responses.add(responses.GET, f'https://viacep.com.br/ws/{cep}/json/',
                      body={json.dumps({'erro': True})}, status=200, content_type="application/json")

        response = self.client.post(
            reverse('moradores_formulario'),  data=morador, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moradores_formulario.html')
        self.assertEqual(
            response.context['erro'], 'Você digitou um CEP invalido. Tente novamente.')

        responses.reset()


class GetBairroViewTest(TestCase):
    def setUp(self):
        self.faker = Faker(["pt_BR"])

        cep = self.faker.postcode()

        self.bairro = Bairro.objects.create(
            bairro=self.faker.bairro(),
            cep=cep,
            logradouro=self.faker.street_name(),
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(
            '/moradores/get_bairro/?' + urlencode({'cep': self.bairro.cep}))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse('get_bairro') + '?' + urlencode({'cep': self.bairro.cep}))
        self.assertEqual(response.status_code, 200)

    def test_view_returns_data_correctly(self):
        response = self.client.get(
            reverse('get_bairro') + '?' + urlencode({'cep': self.bairro.cep}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['bairro'], self.bairro.pk)
        self.assertEqual(response.json()['bairros'], [
                         [self.bairro.pk, self.bairro.bairro]])

    def test_view_returns_data_correctly_when_cep_is_missing(self):
        response = self.client.get(reverse('get_bairro'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['bairro'], None)
        self.assertEqual(response.json()['bairros'], [
                         [self.bairro.pk, self.bairro.bairro]])

    def test_view_create_bairro_correctly(self):
        bairro = {'cep': self.faker.postcode(), 'bairro': self.faker.bairro(),
                  'logradouro': self.faker.street_name()}
        response = self.client.get(
            reverse('get_bairro') + '?' + urlencode(bairro))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['bairro'], 2)
        self.assertEqual(response.json()['bairros'], [
                         [self.bairro.pk, self.bairro.bairro], [2, bairro['bairro']]])

    def test_view_returns_error_when_method_isnt_allowed(self):
        response = self.client.post(reverse('get_bairro'))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json()['error'], 'Método não permitido')
