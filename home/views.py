from django.views.generic import DetailView
from datetime import date
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