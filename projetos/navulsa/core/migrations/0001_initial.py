# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pessoa'
        db.create_table(u'core_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11)),
        ))
        db.send_create_signal(u'core', ['Pessoa'])


    def backwards(self, orm):
        # Deleting model 'Pessoa'
        db.delete_table(u'core_pessoa')


    models = {
        u'core.pessoa': {
            'Meta': {'ordering': "['nome', 'cpf']", 'object_name': 'Pessoa'},
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['core']