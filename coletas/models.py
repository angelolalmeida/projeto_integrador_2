
from django.db import models

class Coleta(models.Model):
    DATA_CHOICES = (
        ('toneladas', 'Toneladas'),
        ('quilo', 'Quilo'),
    )

    data_coleta = models.DateField()
    bairro = models.CharField(max_length=100)
    quantidade_coletada = models.FloatField()
    unidade_medida = models.CharField(max_length=10, choices=DATA_CHOICES, default='toneladas')
