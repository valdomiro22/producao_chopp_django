from django import forms
from .models import Barril


class AdicionarBarrilForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=50)
    volume = forms.IntegerField(label='Volume')


class EditarBarrilForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=50)
    volume = forms.IntegerField(label='Volume')