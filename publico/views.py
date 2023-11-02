from django.shortcuts import render
from .forms import MoradoresForm
from django.shortcuts import redirect
from moradores.models import Bairro
import requests
import json
import pandas as pd
import plotly.express as px
from plotly.offline import plot


# Função para criar um gráfico de barras otimizada
def create_bar_chart(data, x, y, title, colors=None):
    df = pd.DataFrame(data)
    df = df.groupby(x)[y].sum().reset_index()
    df = df.sort_values(by=y, ascending=True)
    # fig = px.bar(data_frame=df, y=x, x=y, title=title, text_auto='')
    fig = px.bar(data_frame=df, x=x, y=y,
                 title=title, text_auto='')

    fig.update_layout(
        plot_bgcolor='#f8f9fa',  # Cor de fundo
        # Cor de fundo do papel (área ao redor do gráfico)
        paper_bgcolor='#f8f9fa',
        font_color='#027640',  # Cor do texto
        xaxis_showgrid=True,  # Exibir grade no eixo x
        yaxis_showgrid=True,  # Exibir grade no eixo y
        xaxis_gridwidth=0.5,  # Largura das linhas de grade no eixo x
        yaxis_gridwidth=0.5,  # Largura das linhas de grade no eixo y
        xaxis_gridcolor='#1bfa92',  # Cor das linhas de grade no eixo x
        yaxis_gridcolor='#1bfa92'  # Cor das linhas de grade no eixo y
    )
# marker_color='#284CBA'
    fig.update_traces(textangle=0, textposition="auto",
                      cliponaxis=False, marker_color=colors)

    fig.update_layout(font=dict(family="Ubuntu"))

    return plot(fig, output_type="div")


def index(request):
    return render(request, 'publico_index.html')


def sobre(request):
    return render(request, 'publico_sobre.html')


def agenda(request):
    return render(request, 'publico_agenda.html')


def materiais(request):
    return render(request, 'publico_materiais.html')


def participe(request):
    form = MoradoresForm(request.POST or None)

    if form.is_valid():
        morador = form.save(commit=False)
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

                morador.bairro = bairro
                morador.rua = logradouro
                morador.save()
                return redirect('participe_sucesso')
            else:
                form.add_error(
                    'cep', "Não foi possível salvar, CEP não encontrado.")
        except json.JSONDecodeError:
            form.add_error('cep', "O CEP fornecido não é válido.")

    context = {'form': form}
    return render(request, 'publico_participe.html', context)


def participe_sucesso(request):
    return render(request, 'publico_participe_sucesso.html')


def reciclometro(request):
    # Cria gráficos com os principais dados

    # Reciclado x não reciclado
    reciclado_versus_nao_reciclado = [
        {
            'Tipo': 'Lixo Coletado',
            'Qtde(ton)': 9.8,
        },
        {
            'Tipo': 'Lixo Reciclado',
            'Qtde(ton)': 0.8,
        },
        {
            'Tipo': 'Lixo que poderia ser reciclado',
            'Qtde(ton)': 2.94,
        },
    ]

    cores_grafico = ['#027640', '#6b04c5', '#c56b04']

    reciclado_versus_nao_reciclado_plot = create_bar_chart(
        reciclado_versus_nao_reciclado, 'Tipo', 'Qtde(ton)', 'Lixo reciclado x não reciclado', colors=cores_grafico)

    context = {
        'reciclado_versus_nao_reciclado_plot': reciclado_versus_nao_reciclado_plot,

    }

    return render(request, 'publico_nossos_numeros.html', context=context)
