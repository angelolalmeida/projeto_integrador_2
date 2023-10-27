from django.db import models
from django.utils import timezone
from moradores.models import Bairro
from cpf_field.models import CPFField

STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('verificando', 'Verificando'),
    ('resolvido', 'Resolvido'),
]

TIPO_RECLAMACAO_CHOICES = [
    ('nao_recebi_saco', 'NÃO RECEBI O SACO VERDE'),
    ('caminhao_nao_passou', 'CAMINHÃO NÃO PASSOU'),
    ('saco_rasgado', 'SACO VERDE RASGADO'),
    ('saco_insuficiente', 'SACO VERDE INSUFICIENTE'),
    ('sugestao', 'SUGESTÃO'),
    ('outros', 'OUTRO'),
]

class Reclamacoes(models.Model):
    nome = models.CharField(max_length=100, null=True, verbose_name="NOME COMPLETO")
    cpf = CPFField('CPF')
    acompanhar_reclamacao = models.BooleanField(default=False, verbose_name="ACOMPANHAR RECLAMAÇÃO")
    tipo_reclamacao = models.CharField(max_length=20, choices=TIPO_RECLAMACAO_CHOICES, verbose_name="TIPO DE RECLAMAÇÃO")
    observacao = models.TextField(max_length=500, verbose_name="DETALHES DA RECLAMAÇÃO")
    cep = models.CharField(max_length=100, null=True, verbose_name="CEP")
    rua = models.CharField(max_length=200, blank=True, verbose_name="RUA")
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, verbose_name="BAIRRO")
    numero_casa = models.CharField(max_length=10, blank=True, verbose_name="NÚMERO DA CASA")
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name="COMPLEMENTO")
    referencia = models.CharField(max_length=100, blank=True, null=True, verbose_name="PONTO DE REFERÊNCIA")
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="TELEFONE")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', verbose_name="STATUS")
    historico = models.TextField(blank=True, null=True, default='', verbose_name="RESPOSTA")
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="DATA DA RECLAMAÇÃO")

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reclamação de {self.nome}"

    class Meta:
        db_table = ''
        verbose_name_plural = ''
        verbose_name = ''
