from django import forms
from .models import Quantidade

class QuantidadeForm(forms.ModelForm):
    class Meta:
        model = Quantidade
        fields = ['quantidade']