# Generated by Django 4.2 on 2023-05-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_incidenciapornotificar_incidencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='image',
            field=models.TextField(),
        ),
    ]
