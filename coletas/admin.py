from django.contrib import admin
from coletas import models


@admin.register(models.Coleta)
class ColetasAdmin(admin.ModelAdmin):
    list_display = ('data_coleta', 'quantidade_coletada', 'bairro')
    ordering = ('-data_coleta',)
    search_fields = ('data_coleta', 'bairro')
    list_per_page = 10
    # list_filter = ('data_coleta')
    list_max_show_all = 10
    # list_display_links = ('data_coleta')

    def has_delete_permission(self, request, obj=None):
        return False
