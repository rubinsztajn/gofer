# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tags'
        db.create_table(u'metadata_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'metadata', ['Tags'])

        # Deleting field 'Image.filename'
        db.delete_column(u'metadata_image', 'filename')

        # Adding field 'Image.original_path'
        db.add_column(u'metadata_image', 'original_path',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Record.place'
        db.add_column(u'metadata_record', 'place',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Record.notes'
        db.add_column(u'metadata_record', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Record.record_status'
        db.add_column(u'metadata_record', 'record_status',
                      self.gf('django.db.models.fields.CharField')(default=('d', 'Draft'), max_length=1),
                      keep_default=False)

        # Adding M2M table for field tags on 'Record'
        db.create_table(u'metadata_record_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm[u'metadata.record'], null=False)),
            ('tags', models.ForeignKey(orm[u'metadata.tags'], null=False))
        ))
        db.create_unique(u'metadata_record_tags', ['record_id', 'tags_id'])


    def backwards(self, orm):
        # Deleting model 'Tags'
        db.delete_table(u'metadata_tags')

        # Adding field 'Image.filename'
        db.add_column(u'metadata_image', 'filename',
                      self.gf('django.db.models.fields.CharField')(default='ex', max_length=100),
                      keep_default=False)

        # Deleting field 'Image.original_path'
        db.delete_column(u'metadata_image', 'original_path')

        # Deleting field 'Record.place'
        db.delete_column(u'metadata_record', 'place')

        # Deleting field 'Record.notes'
        db.delete_column(u'metadata_record', 'notes')

        # Deleting field 'Record.record_status'
        db.delete_column(u'metadata_record', 'record_status')

        # Removing M2M table for field tags on 'Record'
        db.delete_table('metadata_record_tags')


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
            'date_created': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date_issued': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
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