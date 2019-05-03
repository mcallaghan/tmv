# Generated by Django 2.2 on 2019-04-26 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0273_studyeffect_docmetacoding'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyeffect',
            name='editing_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='studyeffect',
            name='editing_time_elapsed',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='studyeffect',
            name='finish_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='studyeffect',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]