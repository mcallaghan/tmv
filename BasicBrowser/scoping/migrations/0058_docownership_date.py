# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-14 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0057_auto_20170313_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='docownership',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Rating Date'),
        ),
    ]
