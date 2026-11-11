from django.db import transaction
from django.db.models import Sum
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import QuantidadeForm
from .enums import TipoQuantidade
from .models import Producao, Quantidade


class ListaProducoesView(ListView):
    model = Producao
    template_name = 'lista-producoes.html'
    context_object_name = 'producoes'

    def get_queryset(self):
        return Producao.objects.filter(grade_id=self.kwargs['grade_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grade_id'] = self.kwargs['grade_id']
        return context


class AdicionarProducaosView(CreateView):
    model = Producao
    template_name = 'adicionar-producao.html'
    fields = ['barril', 'produto', 'quantidade_programada', 'quantidade_produzida']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barril'].empty_label = 'Selecione um barril'
        form.fields['produto'].empty_label = 'Selecione um produto'
        return form

    @transaction.atomic
    def form_valid(self, form):
        form.instance.grade_id = self.kwargs['grade_id']
        response = super().form_valid(form)

        if self.object.quantidade_produzida > 0:
            Quantidade.objects.create(
                producao=self.object,
                quantidade=self.object.quantidade_produzida,
                tipo=TipoQuantidade.DEFINICAO_INICIAL
            )

        return response

    def get_success_url(self):
        return reverse('lista-producoes', kwargs={'grade_id': self.object.grade_id})


class EditarProducaoView(UpdateView):
    model = Producao
    template_name = 'editar-producao.html'
    fields = ['grade', 'barril', 'produto', 'quantidade_programada', 'quantidade_produzida']

    @transaction.atomic
    def form_valid(self, form):
        quantidade_anterior = Producao.objects.get(pk=self.object.pk).quantidade_produzida
        response = super().form_valid(form)

        quantidade_nova = self.object.quantidade_produzida

        if quantidade_anterior != quantidade_nova:
            Quantidade.objects.create(
                producao=self.object,
                quantidade=quantidade_nova - quantidade_anterior,
                tipo=TipoQuantidade.AJUSTE_CORRECAO
            )

        return response

    def get_success_url(self):
        return reverse('lista-producoes', kwargs={'grade_id': self.object.grade_id})


class DeletarProducaosView(DeleteView):
    model = Producao

    def get_success_url(self):
        return reverse('lista-producoes', kwargs={'grade_id': self.object.grade_id})


class AdicionarQuantidadeView(CreateView):
    model = Quantidade
    form_class = QuantidadeForm

    @transaction.atomic
    def form_valid(self, form):
        form.instance.producao_id = self.kwargs['producao_id']
        tipo = self.request.POST.get('tipo')

        if tipo not in [TipoQuantidade.SOMA, TipoQuantidade.SUBTRACAO]:
            form.add_error(None, 'Tipo de movimentação inválido.')
            return self.form_invalid(form)

        quantidade = abs(form.cleaned_data['quantidade'])

        if tipo == TipoQuantidade.SUBTRACAO:
            quantidade = -quantidade

        form.instance.quantidade = quantidade
        form.instance.tipo = tipo

        producao = Producao.objects.select_for_update().get(pk=form.instance.producao_id)

        if producao.quantidade_produzida + quantidade < 0:
            form.add_error('quantidade', 'A quantidade produzida não pode ficar negativa.')
            return self.form_invalid(form)

        response = super().form_valid(form)

        producao.quantidade_produzida += quantidade
        producao.save(update_fields=['quantidade_produzida', 'editado_em'])

        return response

    def get_success_url(self):
        return reverse('home', kwargs={'producao_id': self.object.producao_id})


class ListaQuantidadesView(ListView):
    model = Quantidade
    template_name = 'historico.html'
    context_object_name = 'quantidades'

    def get_queryset(self):
        return Quantidade.objects.filter(
            producao_id=self.kwargs['producao_id']
        ).order_by('-criado_em')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producao_id'] = self.kwargs['producao_id']
        context['soma'] = self.get_queryset().aggregate(total=Sum('quantidade'))['total'] or 0
        return context
