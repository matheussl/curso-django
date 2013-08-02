# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        Pessoa = orm['core.Pessoa']
        Pessoa.objects.all().update(nome='Matheus')

    def backwards(self, orm):
        Pessoa = orm['core.Pessoa']
        Pessoa.objects.all().delete()

    models = {
        u'core.pessoa': {
            'Meta': {'ordering': "['nome', 'cpf']", 'object_name': 'Pessoa'},
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'endereco': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['core']
    symmetrical = True
