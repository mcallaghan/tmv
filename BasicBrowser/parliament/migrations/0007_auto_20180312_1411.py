# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0006_auto_20180312_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interjection',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='interjection',
            name='parties',
        ),
        migrations.RemoveField(
            model_name='interjection',
            name='persons',
        ),
        migrations.AlterField(
            model_name='reaction',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Interjection',
        ),
    ]