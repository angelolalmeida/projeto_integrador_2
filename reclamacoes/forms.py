from django import forms
from django.core.exceptions import ValidationError
from .models import Reclamacoes

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError('CPF deve conter exatamente 11 dígitos.')

class ReclamacoesForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF',validators=[validate_cpf], widget=forms.TextInput(attrs={'id': 'id_cpf'}), required=False)
    acompanhareclamacao = forms.BooleanField(label='PARA ACOMPANHAR SUA RECLAMAÇÃO SELECIONE A OPÇÃO E PRENCHA SEU CPF',required=False, widget=forms.CheckboxInput(attrs={'id': 'id_acompanhareclamacao'}))

    class Meta:
        model = Reclamacoes
        fields = ['nome','tipo_reclamacao', 'observacao',
                  'cep', 'rua', 'numero_casa', 'complemento',
                  'referencia', 'telefone', 'acompanhareclamacao','cpf',]
        labels = {'acompanhareclamacao':'OPCIONAL','telefone': 'TELEFONE','complemento': 'COMPLEMENTO','numero_casa': 'NÚMERO CASA','rua': 'RUA','cep': 'CEP','nome': 'NOME','cpf': 'CPF','observacao': 'DETALHES DA RECLAMAÇÃO','tipo_reclamacao': 'TIPO DE RECLAMAÇÃO', 'numero_casa': 'NÚMERO DA CASA','referencia':'PONTO DE REFERÊNCIA' }
        help_texts = {}

    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        acompanhareclamacao = cleaned_data.get('acompanhareclamacao')

        if acompanhareclamacao and not cpf:
            self.add_error('cpf', 'CPF é obrigatório quando a opção CPF Opcional está selecionada.')
