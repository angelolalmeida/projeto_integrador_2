from django.test import TestCase
from faker import Faker

from moradores.models import Bairro
from reclamacoes.models import Reclamacoes


class ReclamacoesTestCase(TestCase):
    def setUp(self):
        faker = Faker(['pt_BR'])

        bairro = Bairro.objects.create(
            bairro=faker.bairro(),
            cep=faker.postcode(),
            logradouro=faker.street_name(),
        )

        self.reclamacao = Reclamacoes.objects.create(
            nome=faker.name(),
            cpf=faker.cpf(),
            tipo_reclamacao=faker.word(),
            observacao=faker.text(200),
            bairro=bairro
        )

    def test_object_name_is_nome_bairro(self):
        expected_object_name = f"Reclamação de {self.reclamacao.nome}"
        self.assertEqual(str(self.reclamacao), expected_object_name)
