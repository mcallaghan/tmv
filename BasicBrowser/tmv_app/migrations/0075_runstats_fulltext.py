# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-23 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0074_dynamictopic_wg_prop'),
    ]

    operations = [
        migrations.AddField(
            model_name='runstats',
            name='fullText',
            field=models.BooleanField(default=False, help_text='do analysis on fullText? (dependent on availability)'),
        ),
    ]
