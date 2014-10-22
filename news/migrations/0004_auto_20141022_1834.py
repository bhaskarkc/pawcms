# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'get_latest_by': 'date', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 10, 22, 18, 34, 1, 486895)),
        ),
    ]
