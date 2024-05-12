from django.test import TestCase
from faker import Faker

from moradores.models import Bairro
from moradores.models import Morador


class BairroTestCase(TestCase):
    def setUp(self):
        faker = Faker(["pt_BR"])

        self.bairro = Bairro.objects.create(
            bairro=faker.bairro(),
            cep=faker.postcode(),
            logradouro=faker.street_name(),
        )

    def test_object_name_is_nome_bairro(self):
        expected_object_name = self.bairro.bairro
        self.assertEqual(str(self.bairro), expected_object_name)


class MoradorTestCase(TestCase):
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

    def test_object_name_is_nome_morador(self):
        expected_object_name = self.morador.nome
        self.assertEqual(str(self.morador), expected_object_name)
