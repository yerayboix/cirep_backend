# Generated by Django 4.2 on 2023-05-10 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoIncidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de incidencia',
                'verbose_name_plural': 'Tipos de incidencias',
            },
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='report_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.tipoincidencia'),
        ),
    ]