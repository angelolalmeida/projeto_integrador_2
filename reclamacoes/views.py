from django.shortcuts import render, redirect
from .models import Reclamacoes
from .forms import ReclamacoesForm
from moradores.models import Bairro
import requests
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class ReclamacoesListView(ListView, LoginRequiredMixin):
    paginate_by = 8
    model = Reclamacoes

    def get_queryset(self):
        query = self.request.GET.get('cpf')
        queryset = self.model.objects.filter(
            cpf__icontains=query) if query else self.model.objects.none()
        return queryset


def reclamacoes_formulario(request):
    form = ReclamacoesForm(request.POST or None)

    if form.is_valid():
        reclamacao = form.save(commit=False)
        cep = request.POST.get('cep')

        link = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)

        bairro = Bairro.objects.filter(cep='17250000').first()

        try:
            dic_requisicao = json.loads(requisicao.text)
            if requisicao.status_code == 200 and 'erro' not in dic_requisicao:
                bairro_nome = dic_requisicao.get('bairro')
                logradouro = dic_requisicao.get('logradouro')

                verifica_bairro = Bairro.objects.filter(cep=cep).first()

                if verifica_bairro:
                    bairro = verifica_bairro

                else:
                    bairro = Bairro(bairro=bairro_nome, cep=cep,
                                    logradouro=logradouro)
                    bairro.save()

                reclamacao.bairro = bairro
                reclamacao.rua = logradouro
                reclamacao.save()
                return redirect('reclamacoes_lista')
            else:
                form.add_error(
                    'cep', "Não foi possível salvar a reclamação, CEP não encontrado.")
        except json.JSONDecodeError:
            form.add_error('cep', "O CEP fornecido não é válido.")

    context = {'form': form}
    return render(request, 'reclamacoes/reclamacoes_form.html', context)
