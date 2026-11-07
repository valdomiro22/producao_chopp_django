from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producao


class ListaProducoesView(ListView):
    model = Producao
    template_name = 'lista-producoes.html'
    context_object_name = 'producoes'

class AdicionarProducaosView(CreateView):
    model = Producao
    template_name = 'adicionar-producao.html'
    fields = ["grade", "barril", "produto", "quantidade_programada", "quantidade_produzida"]
    success_url = reverse_lazy('lista-producoes')

class EditarProducaoView(UpdateView):
    model = Producao
    template_name = 'editar-producao.html'
    fields = ["grade", "barril", "produto", "quantidade_programada", "quantidade_produzida"]
    success_url = reverse_lazy('lista-producoes')


class DeletarProducaosView(DeleteView):
    model = Producao
    success_url = reverse_lazy('lista-producoes')

