# Generated by Django 2.2.9 on 2020-03-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0326_auto_20200330_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='docusercat',
            name='duration',
            field=models.FloatField(null=True),
        ),
    ]
