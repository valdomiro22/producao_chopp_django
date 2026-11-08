from django.urls import path
from .views import ListaProducoesView, AdicionarProducaosView, EditarProducaoView, DeletarProducaosView


urlpatterns = [
    path('producoes/<int:grade_id>/', ListaProducoesView.as_view(), name='lista-producoes'),
    path('producoes/adicionar', AdicionarProducaosView.as_view(), name='adicionar-producao'),
    path('producoes/editar/<int:pk>', EditarProducaoView.as_view(), name='editar-producao'),
    path('producoes/deletar/<int:pk>', DeletarProducaosView.as_view(), name='deletar-producao'),
]