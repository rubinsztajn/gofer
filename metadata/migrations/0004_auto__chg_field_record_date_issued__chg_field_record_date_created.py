# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Record.date_issued'
        db.alter_column(u'metadata_record', 'date_issued', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Record.date_created'
        db.alter_column(u'metadata_record', 'date_created', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Record.date_issued'
        db.alter_column(u'metadata_record', 'date_issued', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Record.date_created'
        db.alter_column(u'metadata_record', 'date_created', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'metadata.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'original_path': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['metadata.Record']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'metadata.name': {
            'Meta': {'object_name': 'Name'},
            'dates': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        },
        u'metadata.record': {
            'Meta': {'object_name': 'Record'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_issued': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'names': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.Name']", 'symmetrical': 'False', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'record_status': ('django.db.models.fields.CharField', [], {'default': "('d', 'Draft')", 'max_length': '1'}),
            'relatives': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.Related']", 'symmetrical': 'False', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.Tags']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'metadata.related': {
            'Meta': {'object_name': 'Related'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'metadata.tags': {
            'Meta': {'object_name': 'Tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['metadata']