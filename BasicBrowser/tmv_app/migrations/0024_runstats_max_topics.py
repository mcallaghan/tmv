# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0023_runstats_parent_run_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='runstats',
            name='max_topics',
            field=models.IntegerField(null=True),
        ),
    ]
