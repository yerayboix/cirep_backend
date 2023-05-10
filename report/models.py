from django.db import models
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your models here.
# creamos el modelo con los atributos requeridos


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
    report_type = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

