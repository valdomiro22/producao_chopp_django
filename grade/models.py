from django.db import models
from django.db.models import Sum

class Grade(models.Model):
    numero = models.IntegerField('Número')
    data_producao = models.DateField('Data de produção')
    criado_em = models.DateField('Criado em', auto_now_add=True)
    editado_em = models.DateField('Editado em', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return  str(self.numero)

    @property
    def quantidade_barris(self):
        return self.producoes.aggregate(
            total=Sum('quantidade_programada')
        )['total'] or 0

    @property
    def volume_necessario(self):
        return sum(producao.volume_necessario for producao in self.producoes.all())