# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0151_citation_copy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkproperties_copy',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='networkproperties_copy',
            name='network',
        ),
        migrations.DeleteModel(
            name='NetworkProperties_copy',
        ),
    ]