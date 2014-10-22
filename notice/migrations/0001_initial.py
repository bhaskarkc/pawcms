# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import froala_editor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text=b'Leave empty/unchanged for default slug.', max_length=255, null=True, blank=True)),
                ('content', froala_editor.fields.FroalaField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.datetime(2014, 10, 22, 16, 22, 50, 78589))),
                ('status', models.CharField(default=b'Published', max_length=10, choices=[(b'Published', b'Published'), (b'Draft', b'Draft'), (b'Trashed', b'Trashed')])),
                ('comments_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'get_latest_by': 'date',
            },
            bases=(models.Model,),
        ),
    ]
