from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

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

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Grade e produções excluídas com sucesso!")
        return response