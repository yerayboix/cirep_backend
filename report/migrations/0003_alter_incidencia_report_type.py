# Generated by Django 4.2 on 2023-05-10 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_tipoincidencia_alter_incidencia_report_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='report_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.tipoincidencia'),
        ),
    ]