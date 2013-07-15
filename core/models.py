from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.nome, self.descricao[:20])

