from django.contrib import admin
from .models import Producao


@admin.register(Producao)
class ProducaoAdmin(admin.ModelAdmin):
    list_display = ('grade', 'barril', 'produto', 'quantidade_programada', 'quantidade_produzida')