# Generated by Django 4.2 on 2023-05-11 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_poblar_tipo_incidencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidenciapornotificar',
            name='incidencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.incidencia', unique=True),
        ),
    ]
