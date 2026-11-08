from django.views.generic import DetailView
from datetime import date, datetime, timedelta
from django.views.generic import TemplateView
from producao.models import Producao

class HomeView(DetailView):
    model = Producao
    template_name = 'index.html'
    context_object_name = 'producao'
    pk_url_kwarg = 'producao_id'


class VerificarValidade(TemplateView):
    template_name = 'verificar-validade.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data_producao = self.request.GET.get('data_producao')
        data_validade = self.request.GET.get('data_validade')

        if data_producao and data_validade:
            try:
                producao = date.fromisoformat(data_producao)
                validade = date.fromisoformat(data_validade)

                context['dias_restantes'] = (validade - producao).days

            except ValueError:
                context['erro'] = 'Informe datas válidas.'

        return context


from datetime import datetime, timedelta
from django.views.generic import TemplateView


class CalcularTempoParada(TemplateView):
    template_name = 'verificar-tempo-parada.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        horario_inicio = self.request.GET.get('horario_inicio')
        horario_fim = self.request.GET.get('horario_fim')

        if horario_inicio and horario_fim:
            try:
                inicio = datetime.strptime(horario_inicio, '%H:%M')
                fim = datetime.strptime(horario_fim, '%H:%M')

                if fim < inicio:
                    fim += timedelta(days=1)

                diferenca = fim - inicio

                context['horas_parada'] = str(diferenca)

            except ValueError:
                context['erro'] = 'Informe horários válidos.'

        return context
