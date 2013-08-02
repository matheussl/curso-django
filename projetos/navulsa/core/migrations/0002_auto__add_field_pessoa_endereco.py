# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pessoa.endereco'
        db.add_column(u'core_pessoa', 'endereco',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pessoa.endereco'
        db.delete_column(u'core_pessoa', 'endereco')


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