from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import plotly.graph_objects as go
from coletas.models import Coleta
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from datetime import datetime, timedelta


@login_required
def index(request):
    grafico_coletas = gera_grafico_coletas(request)
    context = {
        'grafico_coletas': grafico_coletas,
    }
    return render(request, 'dashboard_index.html', context)


def gera_grafico_coletas(request):

    # Obtenha a data atual e subtraia 12 meses
    data_atual = datetime.now()
    data_inicio = data_atual - timedelta(days=365)

    nomes_meses = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }

    coletas = Coleta.objects.filter(data_coleta__gte=data_inicio).annotate(month=TruncMonth(
        'data_coleta')).values('month').annotate(total=Sum('quantidade_coletada')).order_by('month')

    # Crie listas vazias para armazenar os meses, os totais e as variações
    meses = []
    totais = []
    variacoes = []

    # Preencha as listas com os dados do modelo Coleta e calcule as variações
    for i, coleta in enumerate(coletas):
        mes_numero = coleta['month'].month
        mes_nome = nomes_meses[mes_numero]
        meses.append(mes_nome)
        totais.append(coleta['total'])
        if i > 0:
            variacao = coleta['total'] - coletas[i-1]['total']
            variacoes.append(variacao)

    # Crie o gráfico de linha com marcadores usando o Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses, y=totais,
                  mode='lines+markers', name='Valores Mensais'))
    for i, variacao in enumerate(variacoes):
        fig.add_annotation(
            x=meses[i+1], y=totais[i+1], text=f'Variação: {variacao}', showarrow=True, arrowhead=1)

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
    # Renderize o gráfico no template
    plot_div = fig.to_html(full_html=False)

    return plot_div


def sobre_o_projeto(request):
    return render(request, 'sobre_o_projeto.html')
