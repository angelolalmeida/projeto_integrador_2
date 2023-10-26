from django.shortcuts import render, redirect
from .models import Reclamacoes
from .forms import ReclamacoesForm
from moradores.models import Bairro
import requests, json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.contrib import messages

class ReclamacoesListView(ListView):
    paginate_by = 8
    model = Reclamacoes    

    def get_queryset(self):
        query = self.request.GET.get('cpf')
        if query:
            queryset = self.model.objects.filter(cpf__icontains=query)
        else:
            queryset = self.model.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def reclamacoes_formulario(request):
    form = ReclamacoesForm()

    if request.method == 'POST':
        form = ReclamacoesForm(request.POST)
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
                        bairro = Bairro(bairro=bairro_nome, cep=cep, logradouro=logradouro)
                        bairro.save()
                    
                    reclamacao.bairro = bairro
                    reclamacao.rua = logradouro
                    reclamacao.save()
                    return redirect('reclamacoes_lista')
                else:
                    messages.error(request, "Não foi possível salvar a reclamação, CEP não encontrado.")
            except json.JSONDecodeError:
                messages.error(request, "O CEP fornecido não é válido.")

    context = {'form': form}
    return render(request, 'reclamacoes/reclamacoes_form.html', context)
