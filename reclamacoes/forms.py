from django import forms
from django.core.exceptions import ValidationError
from .models import Reclamacoes

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError(' Campo CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError(' Campo CPF deve conter exatamente 11 dígitos.')

class ReclamacoesForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF',validators=[validate_cpf], widget=forms.TextInput(attrs={'id': 'id_cpf'}), required=False)
    acompanhar_reclamacao = forms.BooleanField(label='DESEJO ACOMPANHAR MINHA RECLAMAÇÃO.',required=False, widget=forms.CheckboxInput(attrs={'id': 'id_acompanhar_reclamacao'}))

    class Meta:
        model = Reclamacoes
        fields = ['nome','tipo_reclamacao', 'observacao',
                  'cep', 'rua', 'numero_casa', 'complemento',
                  'referencia', 'telefone', 'acompanhar_reclamacao','cpf',]
        labels = {'acompanhar_reclamacao':'OPCIONAL','telefone': 'TELEFONE','complemento': 'COMPLEMENTO','numero_casa': 'NÚMERO CASA','rua': 'RUA','cep': 'CEP','nome': 'NOME COMPLETO','cpf': 'CPF','observacao': 'DETALHES DA RECLAMAÇÃO','tipo_reclamacao': 'TIPO DE RECLAMAÇÃO', 'numero_casa': 'NÚMERO DA CASA','referencia':'PONTO DE REFERÊNCIA' }


    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        acompanhar_reclamacao = cleaned_data.get('acompanhar_reclamacao')

        if acompanhar_reclamacao and not cpf:
            self.add_error('cpf', 'Para acompanhar sua reclamação o campo CPF é obrigatório')
