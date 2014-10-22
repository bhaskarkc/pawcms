# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20141022_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 22, 18, 28, 49, 1067), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(help_text=b'Leave empty/unchanged for default slug.', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 22, 18, 29, 0, 927435), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 22, 18, 29, 8, 242017), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 22, 18, 29, 10, 726427), editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(related_name=b'images', to='gallery.Album'),
        ),
    ]
