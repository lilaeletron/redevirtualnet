# main/forms.py
from django import forms
from .models import Reclamacao, Assinatura  # Você precisará criar esses modelos

class ReclamacaoForm(forms.ModelForm):
    class Meta:
        model = Reclamacao
        fields = ['nome', 'email', 'reclamacao']

class AssinaturaForm(forms.ModelForm):
    class Meta:
        model = Assinatura
        fields = ['plano', 'nome', 'email']
