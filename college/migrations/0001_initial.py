# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_no', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('details', models.TextField()),
                ('photo', models.ImageField(upload_to=b'')),
                ('attachment', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
