# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('coletas/', views.coleta_list, name='coleta_list'),
#     path('coletas.html/', views.coletas_page, name='coletas.html'),
#     # Adicione outras URLs conforme necessário
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.coleta_list, name='coleta_list'),
    #path('coletas/', views.coleta_list, name='coleta_list'),
    #path('coletas/', views.coletas_page, name='coletas'),
    # Adicione outras URLs conforme necessário
]
