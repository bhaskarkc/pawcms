# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20141022_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='thumbnail',
            field=models.ForeignKey(related_name=b'thumbnail_of', blank=True, to='gallery.Image', null=True),
        ),
    ]
