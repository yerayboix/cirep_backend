# Generated by Django 4.2 on 2023-05-12 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_alter_incidencia_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidenciaDesacreditada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_reportes', models.IntegerField(default=0)),
                ('incidencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.incidencia')),
            ],
            options={
                'verbose_name': 'Incidencia desacreditada',
                'verbose_name_plural': 'Incidencias desacreditadas',
            },
        ),
    ]