from cbv.forms import PessoaForm
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.urls  import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *

# Create your views here.

# CRIANDO E LISTANDO NA MESMA TEMPLATE
class IndexView(CreateView):
    template_name = 'index.html'
    model = Pessoa
    form_class = PessoaForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects_pessoas"] = Pessoa.objects.all()
        return context
    