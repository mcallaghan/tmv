# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0014_auto_20161212_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wosarticle',
            name='ga',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wosarticle',
            name='so',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
