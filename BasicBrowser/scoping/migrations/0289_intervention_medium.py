# Generated by Django 2.2 on 2019-06-11 11:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0288_auto_20190611_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='medium',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]