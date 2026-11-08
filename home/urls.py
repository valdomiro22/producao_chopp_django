from django.urls import path
from .views import HomeView, VerificarValidade, CalcularTempoParada

urlpatterns = [
    path('home/<int:producao_id>/', HomeView.as_view(), name='home'),
    path('home/verificar-validade/', VerificarValidade.as_view(), name='verificar-validade'),
    path('home/verificar-tempo-parada/', CalcularTempoParada.as_view(), name='verificar-tempo-parada'),
]