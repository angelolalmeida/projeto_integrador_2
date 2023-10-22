from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coletas/', views.coleta_list, name='coleta_list'),
    # Adicione outras URLs conforme necessário
]
