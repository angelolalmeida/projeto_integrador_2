from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('agenda', views.agenda, name='agenda'),
    path('materiais', views.materiais, name='materiais')
]
