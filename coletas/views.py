from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    # Page from the theme
    return render(request, 'pages/index.html')


def coleta_list(request):
    coletas = Coleta.objects.all()
    return render(request, 'coleta_list.html', {'coletas': coletas})
