from django.urls import path
from .views import ListarProdutosView, AdicionarProdutosView, EditarProdutoView, DeletarProdutosView


urlpatterns = [
    path('produtos/', ListarProdutosView.as_view(), name='lista-produtos'),
    path('produtos/adicionar/', AdicionarProdutosView.as_view(), name='adicionar-produto'),
    path('produtos/editar/<int:pk>/', EditarProdutoView.as_view(), name='editar-produto'),
    path('produtos/deletar/<int:pk>/', DeletarProdutosView.as_view(), name='deletar-produto'),
]
