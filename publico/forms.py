from django import forms
from django.core.exceptions import ValidationError
from moradores.models import Morador
from phonenumber_field.formfields import PhoneNumberField


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('Campo CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError('Campo CPF deve conter exatamente 11 dígitos.')


class MoradoresForm(forms.ModelForm):
    whatsapp = PhoneNumberField(
        region="BR", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Morador
        fields = [
            'nome', 'cep', 'endereco', 'numero_endereco', 'bairro', 'whatsapp',
        ]
        labels = {
            'nome': 'Nome Completo',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'numero_endereco': 'Número',
            'bairro': 'Bairro',
            'whatsapp': 'WhatsApp'
        }
