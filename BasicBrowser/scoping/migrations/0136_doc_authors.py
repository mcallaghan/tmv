# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0135_auto_20171012_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='authors',
            field=models.TextField(null=True),
        ),
    ]
