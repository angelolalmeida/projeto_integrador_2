from django.urls import path

from . import views

urlpatterns = [
    path('', views.moradores_lista, name='moradores_lista'),
    path('formulario/', views.moradores_formulario,
         name='moradores_formulario')
]
