from django.db import models
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core import serializers

from report.models import Incidencia
from report.serializer import IncidenciaSerializer
from user.authentication import CustomUserAuthentication
from user.models import User


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

    @action(methods=['get'], detail=True, url_path='get-reports')
    def get_all_reports(self, request):
        reports = Incidencia.objects.all()
        print(request.data)
        return Response({'reports': reports})

    @action(methods=['get'], detail=True, url_path='get-user-reports')
    def get_user_reports(self, request):
        cua = CustomUserAuthentication()
        request_user = cua.authenticate(request)

        user = User.objects.filter(email=request_user.email).first()
        reports = Incidencia.objects.filter(author=user.email)
        print(request.data)
        return Response({'user_reports': reports})

    @action(methods=['post'], detail=True, url_path='create-report')
    def create_report(self, request):
        cua = CustomUserAuthentication()
        request_user = cua.authenticate(request)

        new_report = Incidencia(
            title=request.data['title'],
            report_date=request.data['report_date'],
            description=request.data['description'],
            image=request.data['image'],
            state=request.data['state'],
            latitude=request.data['latitude'],
            longitude=request.data['longitude'],
            author=request_user.email,
            report_type=request.data['report_type']
        )

        try:
            new_report.save()
            return Response({'report': IncidenciaSerializer(new_report).data})
        except Exception as e:
            print(e)
            return Response({'error': 'Error al guardar incidencia'}, status=status.HTTP_400_BAD_REQUEST)
