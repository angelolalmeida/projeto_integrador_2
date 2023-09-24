from django.db import models

class Bairro(models.Model):
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.bairro


class Morador(models.Model):
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    numero_endereco = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, null=True)
    whatsapp = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

