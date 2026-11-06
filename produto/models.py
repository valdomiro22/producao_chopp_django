from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    validade = models.IntegerField('Validade')
    criado_em = models.DateField('Criado em', auto_now_add=True)
    editado_em = models.DateField('Editado em', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome