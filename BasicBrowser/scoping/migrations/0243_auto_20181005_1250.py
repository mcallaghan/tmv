# Generated by Django 2.0.5 on 2018-10-05 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scoping', '0242_auto_20181005_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('association', models.IntegerField(choices=[(0, 'User inherited'), (1, 'User'), (2, 'Query')], default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Category')),
            ],
        ),
        migrations.CreateModel(
            name='DocUserCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='doc',
            name='category',
        ),
        migrations.AddField(
            model_name='doc',
            name='category',
            field = models.ManyToManyField(
                db_index=True,
                through='scoping.DocCat', to='scoping.Category'
            )
        ),
        migrations.AddField(
            model_name='docusercat',
            name='doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc'),
        ),
        migrations.AddField(
            model_name='docusercat',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Project'),
        ),
        migrations.AddField(
            model_name='docusercat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doccat',
            name='doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc'),
        ),
        migrations.AddField(
            model_name='doccat',
            name='docusercats',
            field=models.ManyToManyField(to='scoping.DocUserCat'),
        ),
    ]
