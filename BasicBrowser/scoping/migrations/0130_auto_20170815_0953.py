# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0129_auto_20170815_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectroles',
            old_name='owner',
            new_name='user',
        ),
    ]
