from django.db import models


class TipoQuantidade(models.TextChoices):
    SOMA = 'SOMA', 'Soma'
    SUBTRACAO = 'SUBTRACAO', 'Subtração'
    DEFINICAO_INICIAL = 'DEFINICAO_INICIAL', 'Definição inicial'
    AJUSTE_CORRECAO = 'AJUSTE_CORRECAO', 'Ajuste / Correção'
