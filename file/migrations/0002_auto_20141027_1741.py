# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='file',
            name='template',
        ),
    ]
