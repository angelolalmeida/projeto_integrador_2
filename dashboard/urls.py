from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('sobre_o_projeto/', views.sobre_o_projeto, name='sobre_o_projeto'),
]
