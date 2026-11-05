from django.urls import path
from .views import ListaBarrisView, AdicionarBarrilView, EditarBarrilView


urlpatterns = [
    path('barris/', ListaBarrisView.as_view(), name='lista-barris'),
    path('barris/adicionar/', AdicionarBarrilView.as_view(), name='adicionar-barril'),
    path('barris/editar/<int:pk>/', EditarBarrilView.as_view(), name='editar-barril'),
]
