from django.urls import path
from . import views

urlpatterns = [
    path('', views.coleta_list, name='coletas_lista'),  # /coletas/
    # path('qualquer_coisa/', views.coleta_list,
    #     name='coletas_lista'),  # /coletas/qualquer_coisa
    # path('coletas/', views.coleta_list, name='coletas_lista'), # /coletas/coletas
    # Adicione outras URLs conforme necessário
]
