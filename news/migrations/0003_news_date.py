# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20141022_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 10, 22, 12, 8, 2, 281560)),
            preserve_default=True,
        ),
    ]
