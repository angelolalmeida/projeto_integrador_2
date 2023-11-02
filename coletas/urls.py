from django.urls import path
from . import views

urlpatterns = [
    path('', views.coleta_list, name='coletas_lista'),    
]

