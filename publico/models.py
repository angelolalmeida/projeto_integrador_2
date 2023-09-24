from django.db import models

# Create your models here.
def Teste(models.Model):
    nome = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=1000)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome