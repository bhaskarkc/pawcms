# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sociallinks',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='enabled',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
