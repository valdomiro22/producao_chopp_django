from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Producao


class ListaProducoesView(ListView):
    model = Producao
    template_name = 'lista-producoes.html'
    context_object_name = 'producoes'

    def get_queryset(self):
        grade_id = self.kwargs.get('grade_id')
        return Producao.objects.filter(grade_id=grade_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grade_id'] = self.kwargs.get('grade_id')
        return context


class AdicionarProducaosView(CreateView):
    model = Producao
    template_name = 'adicionar-producao.html'
    fields = ["barril", "produto", "quantidade_programada", "quantidade_produzida"]

    def form_valid(self, form):
        form.instance.grade_id = self.kwargs.get('grade_id')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lista-producoes', kwargs={'grade_id': self.object.grade_id})


class EditarProducaoView(UpdateView):
    model = Producao
    template_name = 'editar-producao.html'
    fields = ["grade", "barril", "produto", "quantidade_programada", "quantidade_produzida"]

    def get_success_url(self):
        return reverse('lista-producoes', kwargs={'grade_id': self.object.grade_id})


class DeletarProducaosView(DeleteView):
    model = Producao

    def get_success_url(self):
        return reverse('lista-producoes', kwargs={'grade_id': self.object.grade_id})