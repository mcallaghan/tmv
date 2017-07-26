# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-20 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0121_auto_20170720_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True)),
                ('fvalue', models.FloatField(null=True)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Network')),
            ],
        ),
    ]