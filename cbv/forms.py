from django import forms
from django.forms import fields
from .models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
