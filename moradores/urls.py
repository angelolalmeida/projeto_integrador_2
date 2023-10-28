from django.urls import path

from . import views

urlpatterns = [
    path('', views.moradores_lista, name='moradores_lista'),
    path('formulario/', views.moradores_formulario,
         name='moradores_formulario'),
    path('editar/<int:morador_id>/', views.moradores_edicao, name='moradores_edicao'),
    path('excluir_morador/<int:morador_id>/', views.excluir_morador, name='excluir_morador')
]
