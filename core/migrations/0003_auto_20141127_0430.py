# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20141127_0430'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialLinks',
            new_name='SocialLink',
        ),
    ]
