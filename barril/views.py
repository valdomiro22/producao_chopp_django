from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Barril


class ListaBarrisView(ListView):
    model = Barril
    template_name = 'lista-barris.html'
    context_object_name = 'barris'


class AdicionarBarrilView(CreateView):
    model = Barril
    template_name = 'adicionar-barril.html'
    fields = ['nome', 'volume', 'descartavel']
    success_url = reverse_lazy('lista-barris')


class EditarBarrilView(UpdateView):
    model = Barril
    template_name = 'editar-barril.html'
    fields = ['nome', 'volume', 'descartavel']
    success_url = reverse_lazy('lista-barris')