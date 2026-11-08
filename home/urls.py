from django.urls import path
from .views import HomeView

urlpatterns = [
    path('home/<int:producao_id>/', HomeView.as_view(), name='home'),
]