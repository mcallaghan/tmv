# Generated by Django 2.1.2 on 2019-02-11 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0044_merge_20181026_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='parliament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parliament.Parl'),
        ),
    ]