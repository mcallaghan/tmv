# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0164_wosarticle_cr_scopus'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.JournalAbbrev'),
        ),
    ]