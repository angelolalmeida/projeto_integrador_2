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
    nome = models.CharField(max_length=100, null=True)
    cpf = CPFField('cpf')
    acompanhar_reclamacao = models.BooleanField(default=False)
    tipo_reclamacao = models.CharField(max_length=20, choices=TIPO_RECLAMACAO_CHOICES)
    observacao = models.TextField(max_length=500)
    cep = models.CharField(max_length=100, null=True)
    rua = models.CharField(max_length=200, blank=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, editable=False)
    numero_casa = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', editable=False)
    historico = models.TextField(blank=True, null=True, editable=False,default='Aguardando resposta')
    data_criacao = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reclamação {self.id}"

    class Meta:
        db_table = 'reclamacoes'
        verbose_name_plural = 'Reclamações'
        verbose_name = 'Reclamação'
