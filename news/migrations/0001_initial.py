# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text=b'Leave empty/unchanged for default slug.', max_length=255, null=True, blank=True)),
                ('content', froala_editor.fields.FroalaField(null=True, blank=True)),
                ('status', models.CharField(default=b'Published', max_length=10, choices=[(b'Published', b'Published'), (b'Draft', b'Draft'), (b'Trashed', b'Trashed')])),
                ('comments_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
