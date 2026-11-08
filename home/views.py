from django.views.generic import DetailView
from producao.models import Producao

class HomeView(DetailView):
    model = Producao
    template_name = 'index.html'
    context_object_name = 'producao'
    pk_url_kwarg = 'producao_id'