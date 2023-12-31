from django.shortcuts import render, redirect, get_object_or_404
from .models import Morador, Bairro
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def moradores_lista(request):
    moradores = Morador.objects.all().order_by('nome')
    # bairros = Bairro.objects.order_by('bairro')
    contexto = {'moradores': moradores}
    return render(request, 'moradores_lista.html', contexto)


def excluir_morador(request, morador_id):
    morador = get_object_or_404(Morador, pk=morador_id)
    morador.delete()
    return redirect('moradores_lista')


def moradores_edicao(request, morador_id):
    morador = get_object_or_404(Morador, pk=morador_id)

    if request.method == 'GET':
        contexto = {'morador': morador}
        return render(request, 'moradores_edicao.html', contexto)

    elif request.method == 'POST':
        nome_novo = (request.POST.get('nome')).capitalize()
        cep_novo = request.POST.get('cep')
        endereco_novo = request.POST.get('endereco')
        numero_endereco_novo = request.POST.get('numero_endereco')
        whatsapp_novo = request.POST.get('whatsapp')

        morador.nome = nome_novo
        morador.endereco = endereco_novo
        morador.numero_endereco = numero_endereco_novo
        morador.whatsapp = whatsapp_novo
        morador.cep = cep_novo

        link = f'https://viacep.com.br/ws/{cep_novo}/json/'
        requisicao = requests.get(link)

        bairro = Bairro.objects.filter(cep='17250000').first()
        dic_requisicao = requisicao.json()
        print(dic_requisicao)

        if requisicao.status_code == 200 and 'erro' not in dic_requisicao:

            bairro = dic_requisicao['bairro']
            logradouro = dic_requisicao['logradouro']

            # verifica se o bairro já está salvo no BD
            verifica_bairro = Bairro.objects.filter(cep=cep_novo).first()

            if verifica_bairro:
                bairro = verifica_bairro

            else:
                bairro = Bairro(bairro=bairro, cep=cep_novo,
                                logradouro=logradouro)
                bairro.save()
                print(bairro)

            # morador = Morador(nome=nome, cep=cep_novo, endereco=endereco, numero_endereco=numero_endereco, whatsapp=whatsapp)

        else:
            erro = 'Você digitou um CEP invalido. Tente novamente.'
            contexto = {'erro': erro, 'morador': morador}
            return render(request, 'moradores_edicao.html', contexto)

        if requisicao.status_code == 200 and 'erro' not in dic_requisicao:
            morador.bairro = bairro

        morador.save()

        return redirect('moradores_lista')


def moradores_formulario(request):
    if request.method == 'GET':
        return render(request, 'moradores_formulario.html')

    elif request.method == 'POST':
        nome = (request.POST.get('nome')).capitalize()
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        numero_endereco = request.POST.get('numero_endereco')
        whatsapp = request.POST.get('whatsapp')

        link = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)

        bairro = Bairro.objects.filter(cep='17250000').first()
        dic_requisicao = requisicao.json()
        print(dic_requisicao)

        if requisicao.status_code == 200 and 'erro' not in dic_requisicao:

            bairro = dic_requisicao['bairro']
            logradouro = dic_requisicao['logradouro']

            # verifica se o bairro já está salvo no BD
            verifica_bairro = Bairro.objects.filter(cep=cep).first()

            if verifica_bairro:
                bairro = verifica_bairro

            else:
                bairro = Bairro(bairro=bairro, cep=cep, logradouro=logradouro)
                bairro.save()
                print(bairro)

            morador = Morador(nome=nome, cep=cep, endereco=endereco,
                              numero_endereco=numero_endereco, whatsapp=whatsapp)

        else:
            erro = 'Você digitou um CEP invalido. Tente novamente.'
            contexto = {'erro': erro}
            return render(request, 'moradores_formulario.html', contexto)

        if requisicao.status_code == 200 and 'erro' not in dic_requisicao:
            morador.bairro = bairro

        morador.save()

        return redirect('moradores_lista')


@csrf_exempt
def get_bairro(request):
    if request.method == 'GET':
        cep = request.GET.get('cep', None)
        bairro = request.GET.get('bairro', None)
        logradouro = request.GET.get('logradouro', None)
        if cep is not None:
            try:
                bairro = Bairro.objects.get(cep=cep)

            except Bairro.DoesNotExist:
                # Cria um novo bairro se ele não existir
                bairro = Bairro(cep=cep, bairro=bairro, logradouro=logradouro)
                bairro.save()

            bairro_id = bairro.id
        else:
            bairro_id = None

        bairros = [(b.id, b.bairro) for b in Bairro.objects.all()]
        print(bairros)

        return JsonResponse({'bairro': bairro_id,
                             'bairros': bairros
                             })
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
