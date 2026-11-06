from django.db import models


class Grade(models.Model):
    numero = models.IntegerField('Número')
    data_producao = models.DateField('Data de produção')
    quantidade_barris = models.IntegerField('Quantidade de barris')
    volume_necessario = models.FloatField('Volume necessário')
    criado_em = models.DateField('Criado em', auto_now_add=True)
    editado_em = models.DateField('Editado em', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return  str(self.numero)