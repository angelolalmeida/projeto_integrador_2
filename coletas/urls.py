from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coletas/', views.coleta_list, name='coletas_lista'),
    # Adicione outras URLs conforme necessário
]
