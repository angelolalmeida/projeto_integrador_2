from django.contrib import admin

from reclamacoes import models

# Register your models here.
@admin.register(models.Reclamacoes)
class ReclamacoesAdmin(admin.ModelAdmin):
    ...