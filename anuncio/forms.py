from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = ('autor', 'tipoSv', 'descSv', 'email', 'telefone', 'endereco')