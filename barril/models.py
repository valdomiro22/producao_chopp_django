from django.db import models


class Base(models.Model):
    criado_em = models.DateField('Criado em', auto_now_add=True)
    editado_em = models.DateField('Editado em', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta():
        abstract = True


class Barril(Base):
    nome = models.CharField('Nome', max_length=50)
    volume = models.IntegerField('Volume')
    descartavel = models.BooleanField('Descartável', default=False)

    def __str__(self):
        return self.nome
