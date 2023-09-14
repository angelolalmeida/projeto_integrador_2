from django.db import models

# Create your models here.
TIPO_RECLAMACAO_CHOICES = [
    ('nao_recebi', 'Não recebi o saco verde'),
    ('caminhao_nao_passou', 'Caminhão não passou'),
    ('saco_rasgado', 'Saco rasgado'),
    ('outros', 'Outros'),
]


class Reclamacoes(models.Model):
    tipo_reclamacao = models.CharField(
        max_length=20, choices=TIPO_RECLAMACAO_CHOICES, default='outros',)
    observacao = models.TextField(max_length=500)
    endereco = models.CharField(max_length=200)

    class Meta:
        db_table = 'reclamacoes'
        verbose_name_plural = 'Reclamações'
        verbose_name = 'Reclamação'
        # ordering = ['nome']
