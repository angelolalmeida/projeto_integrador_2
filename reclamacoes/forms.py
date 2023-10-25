from django import forms
from django.core.exceptions import ValidationError
from .models import Reclamacoes

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError('CPF deve conter exatamente 11 dígitos.')

class ReclamacoesForm(forms.ModelForm):
    cpf = forms.CharField(validators=[validate_cpf], widget=forms.TextInput(attrs={'id': 'id_cpf'}))
    cpfOpcional = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'id_cpfOpcional'}))

    class Meta:
        model = Reclamacoes
        fields = ['nome', 'cpf','cpfOpcional','tipo_reclamacao', 'observacao',
                  'cep', 'rua', 'numero_casa', 'complemento',
                  'referencia', 'telefone',]
        labels = {'cpfOpcional':'OPCIONAL','telefone': 'TELEFONE','complemento': 'COMPLEMENTO','numero_casa': 'NÚMERO CASA','rua': 'RUA','cep': 'CEP','nome': 'NOME','cpf': 'CPF','observacao': 'DETALHES DA RECLAMAÇÃO','tipo_reclamacao': 'TIPO DE RECLAMAÇÃO', 'numero_casa': 'NÚMERO DA CASA','referencia':'PONTO DE REFERÊNCIA' }
        help_texts = {}
