from django.shortcuts import render, redirect
from .models import Reclamacoes
from .forms import ReclamacoesForm
from moradores.models import Bairro
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

# Create your views here.


'''def reclamacoes_lista(request):
    reclamacoes = Reclamacoes.objects.order_by('bairro')
    # bairros = Bairro.objects.order_by('bairro')
    contexto = {'reclamacoes': reclamacoes}
    return render(request, 'reclamacoes_lista.html', context=contexto)
'''
class ReclamacoesListView(LoginRequiredMixin, ListView):
    paginate_by = 8
    model = Reclamacoes    

    def get_queryset(self):
        query = self.request.GET.get('nome')
        if query:
            queryset = self.model.objects.filter(nome__icontains=query)
        else:
            queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



def reclamacoes_formulario(request):
    form = ReclamacoesForm
    
    if request.method == 'POST':
        form = ReclamacoesForm(request.POST)
        if form.is_valid():

            reclamacao = form.save(commit=False)
            '''tipo_reclamacao = request.POST.get('tipo_reclamacao')
            observacao = request.POST.get('observacao')
            cep = request.POST.get('cep')
            rua = request.POST.get('rua')
            bairro = request.POST.get('bairro')
            numero_casa = request.POST.get('numero_casa')
            complemento = request.POST.get('complemento')
            referencia = request.POST.get('referencia')
            telefone = request.POST.get('telefone')
            status = request.POST.get('status')
            historico = request.POST.get('historico')
            data_criacao = request.POST.get('data_criacao')'''
            


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
                
            # reclamacoes = Reclamacoes(tipo_reclamacao=tipo_reclamacao, observacao=observacao, cep=cep, rua=rua, bairro=bairro, numero_casa=numero_casa, complemento=complemento, referencia=referencia, telefone=telefone,status=status, historico=historico, data_criacao=data_criacao)
            
            if requisicao.status_code == 200 and 'erro' not in dic_requisicao:
                reclamacao.bairro = bairro
            
            reclamacao.save()

            return redirect('reclamacoes_lista')

        context = {'form': form}
        return render(request, 'requisicoes/requisicoes_form.html', context)





    




