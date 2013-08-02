from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=100, default='')
    # user = model.ForeignKey('auth.User')

    class Meta:
        ordering = ['nome', 'cpf']

    def __str__(self):
        return '%s - %s' % (self.nome, self.cpf)
