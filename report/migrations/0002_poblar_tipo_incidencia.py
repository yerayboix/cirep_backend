from django.db import migrations
from django.db.transaction import atomic


@atomic
def load_data(apps, schema_editor):
    TipoIncidencia = apps.get_model('report', 'TipoIncidencia')
    options = [
        'Señal Rota',
        'Daños en la acera',
        'Via en mal estado',
        'Basura o suciedad en la via',
        'Desperfecto en el parque',
        'Alumbrado disfuncional',
        'Animal fallecido',
        'Estructura pública en mal estado',
    ]

    for option in options:
        TipoIncidencia.objects.create(type=option)


class Migration(migrations.Migration):
    dependencies = [
        ('report', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
