from django.shortcuts import render, redirect
from .models import Morador, Bairro
import requests

# Create your views here.


def moradores_lista(request):
    moradores = Morador.objects.order_by('nome')
    # bairros = Bairro.objects.order_by('bairro')
    contexto = {'moradores': moradores}
    return render(request, 'moradores_lista.html', contexto)


def moradores_formulario(request):
    if request.method == 'GET':
        return render(request, 'moradores_formulario.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        numero_endereco = request.POST.get('numero_endereco')
        whatsapp = request.POST.get('whatsapp')



        link = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)
        # print(requisicao.Response)

        bairro = Bairro.objects.filter(cep='17250000').first()
        dic_requisicao = requisicao.json()

        if requisicao.status_code == 200 and 'erro' not in dic_requisicao:            

            bairro = dic_requisicao['bairro']
            logradouro = dic_requisicao['logradouro']

            verifica_bairro = Bairro.objects.filter(cep=cep).first()

            if verifica_bairro:
                bairro = verifica_bairro
            
            else:
                bairro = Bairro(bairro=bairro, cep=cep, logradouro=logradouro)
                bairro.save()
                print(bairro)
            
        morador = Morador(nome=nome, cep=cep, endereco=endereco, numero_endereco=numero_endereco, whatsapp=whatsapp)
        
        if requisicao.status_code == 200 and 'erro' not in dic_requisicao:
            morador.bairro = bairro
        
        morador.save()

        return redirect('moradores_lista')



