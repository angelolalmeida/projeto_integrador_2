from django.db import models
from moradores.models import Bairro


class Coleta(models.Model):
    DATA_CHOICES = (
        ('toneladas', 'Toneladas'),
        ('quilo', 'Quilo'),
    )

    data_coleta = models.DateField()
    bairro = models.CharField(max_length=100)
    # bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, null=True)
    quantidade_coletada = models.FloatField()
    unidade_medida = models.CharField(
        max_length=10, choices=DATA_CHOICES, default='toneladas')
