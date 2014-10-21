# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('content', models.TextField(help_text=b'Full HTML Allowed', null=True, blank=True)),
                ('enabled', models.BooleanField(default=True)),
                ('show_heading', models.BooleanField(default=False)),
                ('html_id', models.CharField(help_text=b"Don't use ID if you are using this snippet more than once in a page.", max_length=254, null=True, verbose_name=b'HTML ID', blank=True)),
                ('html_classes', models.CharField(help_text=b'Space separated class names', max_length=254, null=True, verbose_name=b'HTML Classes', blank=True)),
                ('code_mode', models.BooleanField(default=False, help_text=b'Preserves the content as is.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
