from django.db import models
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your models here.
# creamos el modelo con los atributos requeridos


class TipoIncidencia(models.Model):
    type = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = 'Tipo de incidencia'
        verbose_name_plural = 'Tipos de incidencias'


class Incidencia(models.Model):
    STATE_CHOICES = (
        ('P', 'En proceso'),
        ('A', 'Arreglada'),
        ('PR', 'Pendiente de revisión'),
        ('D', 'Descartada')
    )
    d_s_c = dict(STATE_CHOICES)
    report_date = models.DateField(null=True)
    description = models.TextField()
    image = models.CharField(max_length=255)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()
    author = models.CharField(max_length=255)
    report_type = models.ForeignKey(TipoIncidencia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

