from django.urls import path
from .views import HomeView, VerificarValidade

urlpatterns = [
    path('home/<int:producao_id>/', HomeView.as_view(), name='home'),
    path('home/verificar-validade/', VerificarValidade.as_view(), name='verificar-validade'),
]