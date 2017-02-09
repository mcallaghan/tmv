# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0046_auto_20170209_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='technology',
            field=models.ManyToManyField(to='scoping.Technology'),
        ),
        migrations.AlterField(
            model_name='query',
            name='technology',
            field=models.ManyToManyField(to='scoping.Technology'),
        ),
    ]
