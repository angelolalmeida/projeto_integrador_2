from django.shortcuts import render

# Create your views here.


def reclamacoes_lista(request):
    return render(request, 'reclamacoes_lista.html')


def reclamacoes_formulario(request):
    return render(request, 'reclamacoes_formulario.html')
