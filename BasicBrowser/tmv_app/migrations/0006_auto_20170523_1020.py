# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-23 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0005_runstats_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccorr',
            name='topiccorr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Topiccorr', to='tmv_app.Topic'),
        ),
    ]
