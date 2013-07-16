# -*- coding: utf-8 -*-
from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11,)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuárioos'


    def __str__(self):
        return '%s - %s' % (self.nome, self.cpf)

