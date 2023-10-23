from django.shortcuts import render
from .models import Coleta
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    # Página do tema
    return render(request, 'pages/index.html')

def coleta_list(request):
    coletas = Coleta.objects.all()
    return render(request, 'coleta_list.html', {'coletas': coletas})

def coletas_page(request):
    return render(request, 'coletas.html')
