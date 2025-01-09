# main/forms.py
from django import forms
from .models import Reclamacao, AssinaturaCliente  # Você precisará criar esses modelos


class ReclamacaoForm(forms.ModelForm):
    class Meta:
        model = Reclamacao
        fields = ['nome', 'email', 'reclamacao']


class AssinaturaClienteForm(forms.ModelForm):
    class Meta:
        model = AssinaturaCliente
        fields = ['plano', 'nome', 'email', 'telefone']  # Campos exibidos no formulário
        labels = {
            'plano': 'Selecione o Plano',
            'nome': 'Seu Nome',
            'email': 'Seu E-mail',
            'telefone': 'Seu Telefone (Opcional)',
        }
        widgets = {
            'plano': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }