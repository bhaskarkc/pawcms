# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='code_mode',
        ),
        migrations.AlterField(
            model_name='snippet',
            name='content',
            field=froala_editor.fields.FroalaField(null=True, blank=True),
        ),
    ]
