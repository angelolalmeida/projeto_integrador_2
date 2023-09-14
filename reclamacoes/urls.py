from django.urls import path

from . import views

urlpatterns = [
    path('', views.reclamacoes_lista, name='recla_lista'),
    path('formulario/', views.reclamacoes_formulario,
         name='reclamacaoes_formulario'),
]
