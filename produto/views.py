from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto


class ListarProdutosView(ListView):
    model = Produto
    template_name = 'lista-produtos.html'
    context_object_name = 'produtos'


class AdicionarProdutosView(CreateView):
    model = Produto
    template_name = 'adicionar-produto.html'
    fields = ['nome', 'validade']
    success_url = reverse_lazy('lista-produtos')


class EditarProdutoView(UpdateView):
    model = Produto
    template_name = 'editar-produto.html'
    fields = ['nome', 'validade']
    success_url = reverse_lazy('lista-produtos')


class DeletarProdutosView(DeleteView):
    model = Produto
    success_url = reverse_lazy('lista-produtos')


