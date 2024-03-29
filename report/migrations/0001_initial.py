# Generated by Django 4.2 on 2023-05-10 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(null=True)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('P', 'En proceso'), ('A', 'Arreglada'), ('PR', 'Pendiente de revisión'), ('D', 'Descartada')], default=0, max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('author', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Incidencia',
                'verbose_name_plural': 'Incidencias',
            },
        ),
        migrations.CreateModel(
            name='TipoIncidencia',
            fields=[
                ('type', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Tipo de incidencia',
                'verbose_name_plural': 'Tipos de incidencias',
            },
        ),
        migrations.CreateModel(
            name='IncidenciaPorNotificar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.incidencia')),
            ],
            options={
                'verbose_name': 'Incidencia por notificar',
                'verbose_name_plural': 'Incidencias por notificar',
            },
        ),
        migrations.AddField(
            model_name='incidencia',
            name='report_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.tipoincidencia'),
        ),
    ]
