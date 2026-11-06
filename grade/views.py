from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Grade


class ListaGradesView(ListView):
    model = Grade
    template_name = 'lista_grades.html'
    context_object_name = 'grades'


class AdicionarGradesView(CreateView):
    model = Grade
    template_name = 'adicionar-grade.html'
    fields = ['numero', 'data_producao']
    success_url = reverse_lazy('lista-grades')


class EditarGradeView(UpdateView):
    model = Grade
    template_name = 'editar-grade.html'
    fields = ['numero', 'data_producao']
    success_url = reverse_lazy('lista-grades')


class DeletarGradesView(DeleteView):
    model = Grade
    success_url = reverse_lazy('lista-grades')


