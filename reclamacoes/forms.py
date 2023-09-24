from django.forms import ModelForm
from .models import Reclamacoes


class ReclamacoesForm(ModelForm):
    class Meta:
        model = Reclamacoes
        # data_vencimento = forms.DateField(widget=DateInput())

        fields = ['nome', 'tipo_reclamacao', 'observacao',
                  'cep', 'rua', 'bairro', 'numero_casa', 'complemento',
                    'referencia', 'telefone',]
        labels = {'tipo_reclamacao': 'Tipo da reclamação', 'numero_casa': 'Número da Casa','referencia':'Ponto de Referência' }
        help_texts = {}