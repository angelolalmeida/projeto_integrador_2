from django.urls import path
from .views import ReclamacoesListView
from . import views

urlpatterns = [
    path('', ReclamacoesListView.as_view(), name='reclamacoes_lista'),
    path('formulario/', views.reclamacoes_formulario,
         name='reclamacaoes_formulario'),
]
