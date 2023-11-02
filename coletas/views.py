from django.shortcuts import render
from .models import Coleta
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    # Page from the theme
    return render(request, 'pages/index.html')


def coleta_list(request):
    coletas = Coleta.objects.all()
    return render(request, 'coleta_list.html', {'coletas': coletas})
