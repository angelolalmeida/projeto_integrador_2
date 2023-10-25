from django.forms import ModelForm
from .models import Reclamacoes


class ReclamacoesForm(ModelForm):

    class Meta:
        model = Reclamacoes

        fields = ['nome', 'cpf','cpfOpcional','tipo_reclamacao', 'observacao',
                  'cep', 'rua', 'numero_casa', 'complemento',
                    'referencia', 'telefone',]
        labels = {'cpfOpcional':'OPCIONAL','telefone': 'TELEFONE','complemento': 'COMPLEMENTO','numero_casa': 'NÚMERO CASA','rua': 'RUA','cep': 'CEP','nome': 'NOME','cpf': 'CPF','observacao': 'DETALHES DA RECLAMAÇÃO','tipo_reclamacao': 'TIPO DE RECLAMAÇÃO', 'numero_casa': 'NÚMERO DA CASA','referencia':'PONTO DE REFERÊNCIA' }
        help_texts = {}