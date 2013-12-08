# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Article', fields ['url_slug']
        db.create_index(u'blog_article', ['url_slug'])


    def backwards(self, orm):
        # Removing index on 'Article', fields ['url_slug']
        db.delete_index(u'blog_article', ['url_slug'])


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'template_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'url_slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['blog']