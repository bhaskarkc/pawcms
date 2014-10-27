# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 10, 27, 17, 45, 6, 867801)),
            preserve_default=True,
        ),
    ]
