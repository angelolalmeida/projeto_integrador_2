"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', include('home.urls')),
    path('', include('publico.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('moradores/', include('moradores.urls')),
    path('reclamacoes/', include('reclamacoes.urls')),
    path('coletas/', include('coletas.urls')),
    # Redireciona para a página principal '/'
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path("admin/", admin.site.urls),
    path("", include('admin_soft.urls'))
]
