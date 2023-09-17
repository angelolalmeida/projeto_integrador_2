from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):

    # Page from the theme
    return render(request, 'publico_index.html')


def sobre(request):

    # Page from the theme
    return render(request, 'publico_sobre.html')
