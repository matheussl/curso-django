from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return '%s - %s' % (self.nome, self.cpf)
