# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-24 15:49
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0101_auto_20170522_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='ymentions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
    ]
