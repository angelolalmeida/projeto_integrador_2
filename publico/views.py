from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):

    return render(request, 'publico_index.html')


def sobre(request):

    return render(request, 'publico_sobre.html')


def agenda(request):
    return render(request, 'publico_agenda.html')

def materiais(request):
    return render(request, 'publico_materiais.html')
