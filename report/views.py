from django.db import models
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from report.models import Incidencia
from report.serializer import IncidenciaSerializer


# Create your views here.
class IncidenciaViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer

    # personalizamos el endpoint para cambiar el estado
    @action(methods=['post'], detail=True, url_path='change-state')
    def change_state(self, request, pk=None):
        instance = self.get_object()
        state = request.data.get('state')
        if state not in dict(Incidencia.STATE_CHOICES):
            return Response({'detail': 'Estado inválido'}, status=status.HTTP_400_BAD_REQUEST)
        instance.state = state
        instance.save()
        return Response(self.get_serializer(instance).data)
