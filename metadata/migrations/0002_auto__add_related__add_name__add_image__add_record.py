# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Related'
        db.create_table(u'metadata_related', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'metadata', ['Related'])

        # Adding model 'Name'
        db.create_table(u'metadata_name', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dates', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Name'])

        # Adding model 'Image'
        db.create_table(u'metadata_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['metadata.Record'], blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Image'])

        # Adding model 'Record'
        db.create_table(u'metadata_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_created', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('date_issued', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Record'])

        # Adding M2M table for field names on 'Record'
        db.create_table(u'metadata_record_names', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm[u'metadata.record'], null=False)),
            ('name', models.ForeignKey(orm[u'metadata.name'], null=False))
        ))
        db.create_unique(u'metadata_record_names', ['record_id', 'name_id'])

        # Adding M2M table for field relatives on 'Record'
        db.create_table(u'metadata_record_relatives', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm[u'metadata.record'], null=False)),
            ('related', models.ForeignKey(orm[u'metadata.related'], null=False))
        ))
        db.create_unique(u'metadata_record_relatives', ['record_id', 'related_id'])


    def backwards(self, orm):
        # Deleting model 'Related'
        db.delete_table(u'metadata_related')

        # Deleting model 'Name'
        db.delete_table(u'metadata_name')

        # Deleting model 'Image'
        db.delete_table(u'metadata_image')

        # Deleting model 'Record'
        db.delete_table(u'metadata_record')

        # Removing M2M table for field names on 'Record'
        db.delete_table('metadata_record_names')

        # Removing M2M table for field relatives on 'Record'
        db.delete_table('metadata_record_relatives')


    models = {
        u'metadata.image': {
            'Meta': {'object_name': 'Image'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['metadata.Record']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'metadata.name': {
            'Meta': {'object_name': 'Name'},
            'dates': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'metadata.record': {
            'Meta': {'object_name': 'Record'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date_issued': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'names': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.Name']", 'symmetrical': 'False', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'relatives': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.Related']", 'symmetrical': 'False', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'metadata.related': {
            'Meta': {'object_name': 'Related'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['metadata']