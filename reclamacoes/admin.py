from django.contrib import admin
from reclamacoes import models

@admin.register(models.Reclamacoes)
class ReclamacoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'status')
    ordering = ('-id',)
    search_fields = ('nome', 'status')
    list_per_page = 10
    list_filter = ('status',)
    list_max_show_all = 10
    list_display_links = ('id', 'nome')
    readonly_fields = (
        'nome', 'cpf', 'tipo_reclamacao', 'observacao', 'rua',
        'cep', 'numero_casa', 'bairro', 'complemento', 
        'referencia', 'telefone', 'acompanhar_reclamacao'
    )

    fieldsets = (
        ('MORADOR', {
            'fields': ('nome', 'cpf', 'telefone')
        }),
        ('ENDEREÇO', {
            'fields': ('rua', 'cep', 'numero_casa', 
                       'bairro', 'complemento', 'referencia')
        }),
        ('RECLAMAÇÃO', {
            'fields': ('tipo_reclamacao', 'observacao')
        }),
        ('RESPOSTA', {
            'fields': ('status', 'historico')
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False
