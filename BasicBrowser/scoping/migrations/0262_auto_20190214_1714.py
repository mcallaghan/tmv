# Generated by Django 2.1.2 on 2019-02-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0261_note_utterance'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cred_org',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cred_pwd',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cred_uname',
            field=models.TextField(null=True),
        ),
    ]
