from django.db import models
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your models here.
# creamos el modelo con los atributos requeridos


class Incidencia(models.Model):
    STATE_CHOICES = (
        ('P', 'En proceso'),
        ('A', 'Arreglado')
    )

    id = models.CharField(max_length=50, primary_key=True)
    image = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

