from django.urls import path
from .views import ListaGradesView, AdicionarGradesView, EditarGradeView, DeletarGradesView


urlpatterns = [
    path('grades/', ListaGradesView.as_view(), name='lista-grades'),
    path('grades/adicionar/', AdicionarGradesView.as_view(), name='adicionar-grade'),
    path('grades/editar/<int:pk>/', EditarGradeView.as_view(), name='editar-grade'),
    path('grades/deletar/<int:pk>/', DeletarGradesView.as_view(), name='deletar-grade'),
]