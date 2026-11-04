from django.contrib import admin
from .models import Barril

@admin.register(Barril)
class BarrilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'volume', 'descartavel')
