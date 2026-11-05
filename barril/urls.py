from django.urls import path
from .views import ListaBarrisView, AdicionarBarrilView, EditarBarrilView, DeletarBarrilView


urlpatterns = [
    path('barris/', ListaBarrisView.as_view(), name='lista-barris'),
    path('barris/adicionar/', AdicionarBarrilView.as_view(), name='adicionar-barril'),
    path('barris/editar/<int:pk>/', EditarBarrilView.as_view(), name='editar-barril'),
    path('barris/deletar/<int:pk>/', DeletarBarrilView.as_view(), name='deletar-barril'),
]
