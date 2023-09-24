from django.db import models
from django.utils import timezone
from moradores.models import Bairro

# Create your models here.
STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('verificado', 'Verificado'),
        ('resolvido', 'Resolvido'),
        ('nao_resolvido', 'Não Resolvido'),
    ]

TIPO_RECLAMACAO_CHOICES = [
    ('nao_recebi', 'Não recebi o saco verde'),
    ('caminhao_nao_passou', 'Caminhão não passou'),
    ('saco_rasgado', 'Saco rasgado'),
    ('outros', 'Outros'),
]


class Reclamacoes(models.Model):
    nome = models.CharField(max_length=100,null=True)
    tipo_reclamacao = models.CharField(max_length=20, choices=TIPO_RECLAMACAO_CHOICES, default='outros',)
    observacao = models.TextField(max_length=500)
    cep = models.CharField(max_length=100, null=True)
    rua = models.CharField(max_length=200, blank=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    numero_casa = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', editable=False)
    historico = models.TextField(blank=True, null=True, editable=False)
    data_criacao = models.DateTimeField(default=timezone.now, editable=False)

    # Outros campos do modelo Reclamacao

    def __str__(self):
        return f"Reclamação {self.id}"

    class Meta:
        db_table = 'reclamacoes'
        verbose_name_plural = 'Reclamações'
        verbose_name = 'Reclamação'
        # ordering = ['nome']