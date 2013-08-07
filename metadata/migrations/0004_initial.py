# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Name'
        db.create_table(u'metadata_name', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dates', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Name'])

        # Adding model 'Related'
        db.create_table(u'metadata_related', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'metadata', ['Related'])

        # Adding model 'Tags'
        db.create_table(u'metadata_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'metadata', ['Tags'])

        # Adding model 'Record'
        db.create_table(u'metadata_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_created', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('date_issued', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('record_status', self.gf('django.db.models.fields.CharField')(default=('d', 'Draft'), max_length=1)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('rights', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('folder1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('folder2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('orig_path', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('item_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Record'])

        # Adding M2M table for field tags on 'Record'
        db.create_table(u'metadata_record_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm[u'metadata.record'], null=False)),
            ('tags', models.ForeignKey(orm[u'metadata.tags'], null=False))
        ))
        db.create_unique(u'metadata_record_tags', ['record_id', 'tags_id'])

        # Adding M2M table for field relatives on 'Record'
        db.create_table(u'metadata_record_relatives', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm[u'metadata.record'], null=False)),
            ('related', models.ForeignKey(orm[u'metadata.related'], null=False))
        ))
        db.create_unique(u'metadata_record_relatives', ['record_id', 'related_id'])

        # Adding model 'Role'
        db.create_table(u'metadata_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['metadata.Name'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['metadata.Record'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Role'])

        # Adding model 'Image'
        db.create_table(u'metadata_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
            ('original_path', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['metadata.Record'], blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Name'
        db.delete_table(u'metadata_name')

        # Deleting model 'Related'
        db.delete_table(u'metadata_related')

        # Deleting model 'Tags'
        db.delete_table(u'metadata_tags')

        # Deleting model 'Record'
        db.delete_table(u'metadata_record')

        # Removing M2M table for field tags on 'Record'
        db.delete_table('metadata_record_tags')

        # Removing M2M table for field relatives on 'Record'
        db.delete_table('metadata_record_relatives')

        # Deleting model 'Role'
        db.delete_table(u'metadata_role')

        # Deleting model 'Image'
        db.delete_table(u'metadata_image')


    models = {
        u'metadata.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        },
        u'metadata.record': {
            'Meta': {'object_name': 'Record'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date_issued': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'folder1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'folder2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'names': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.Name']", 'symmetrical': 'False', 'through': u"orm['metadata.Role']", 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'orig_path': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'record_status': ('django.db.models.fields.CharField', [], {'default': "('d', 'Draft')", 'max_length': '1'}),
            'relatives': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.Related']", 'symmetrical': 'False', 'blank': 'True'}),
            'rights': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        u'metadata.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['metadata.Name']"}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['metadata.Record']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        },
        u'metadata.tags': {
            'Meta': {'object_name': 'Tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['metadata']