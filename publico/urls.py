from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('agenda', views.agenda, name='agenda'),
    path('materiais', views.materiais, name='materiais'),
    path('participe', views.participe, name='participe'),
    path('participe/sucesso', views.participe_sucesso, name='participe_sucesso'),
    path('reciclometro', views.reciclometro, name='reciclometro'),
    path('reclamacao', views.reclamacao, name='reclamacao'),
    path('reclamacao/consultar', views.reclamacoes_consultar,
         name='reclamacao_consultar'),
]
