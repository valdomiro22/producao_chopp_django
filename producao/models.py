from django.db import models


class Producao(models.Model):
    grade = models.ForeignKey('grade.Grade', on_delete=models.CASCADE, related_name='producoes')
    barril = models.ForeignKey('barril.Barril', on_delete=models.PROTECT)
    produto = models.ForeignKey('produto.Produto', on_delete=models.PROTECT)
    quantidade_programada = models.PositiveIntegerField('Quantidade programada')
    quantidade_produzida = models.PositiveIntegerField( 'Quantidade produzida', default=0)
    data_fim_producao = models.DateField( 'Data de fim de produção', null=True, blank=True)
    criado_em = models.DateTimeField( 'Criado em', auto_now_add=True)
    editado_em = models.DateTimeField( 'Editado em', auto_now=True)
    ativo = models.BooleanField( 'Ativo', default=True)

    def __str__(self):
        return f'{self.produto} - {self.quantidade_programada} barris'

    @property
    def quantidade_pendente(self):
        return self.quantidade_programada - self.quantidade_produzida

    @property
    def volume_necessario(self):
        return self.quantidade_programada * self.barril.volume / 100

    @property
    def volume_utilizado(self):
        return self.quantidade_produzida * self.barril.volume / 100

    @property
    def volume_pendente(self):
        return self.quantidade_pendente * self.barril.volume / 100
