# Generated by Django 4.2 on 2023-05-03 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidencia',
            name='title',
        ),
    ]
