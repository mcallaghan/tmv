# Generated by Django 2.1.2 on 2019-03-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0267_auto_20190226_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(db_index=True, null=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='query',
            name='database',
            field=models.CharField(choices=[('WoS', 'Web of Science'), ('Scopus', 'Scopus'), ('intern', 'Internal'), ('pop', 'Publish or Perish'), ('ebsco', 'EBSCO'), ('jstor', 'JSTOR'), ('ovid', 'OVID')], max_length=6, null=True, verbose_name='Query database'),
        ),
    ]
