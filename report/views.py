from typing import List

from django.db.models import QuerySet
from django.http import HttpResponse
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core import serializers

from cirep.helpers.functions import calculate_distance_between_coordinates
from report.models import Incidencia, TipoIncidencia
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
    def change_state(self, request):
        instance = self.get_object()
        state = request.data.get('state')
        if state not in dict(Incidencia.STATE_CHOICES):
            return Response({'detail': 'Estado inválido'}, status=status.HTTP_400_BAD_REQUEST)
        instance.state = state
        instance.save()
        return Response(self.get_serializer(instance).data)

    @action(methods=['get'], detail=True, url_path='get-reports')
    def get_all_reports(self, request):
        # Vamos a obtener las incidencias activas
        reports = Incidencia.objects.exclude(state='D').exclude(state='A')
        data = serializers.serialize('json', reports)
        return HttpResponse(data, content_type='application/json')

    @action(methods=['get'], detail=True, url_path='get-user-reports')
    def get_user_reports(self, request):
        cua = CustomUserAuthentication()
        request_user = cua.authenticate(request)

        user = User.objects.filter(email=request_user.email).first()
        reports = Incidencia.objects.filter(author=user.email)
        data = serializers.serialize('json', reports)
        return HttpResponse(data, content_type='application/json')

    @action(methods=['get'], detail=True, url_path='get-nearby-reports')
    def get_nearby_reports(self, request):
        reports = Incidencia.objects.exclude(state='D').exclude(state='A')
        user_latitude = float(request.data.get('latitude'))
        user_longitude = float(request.data.get('longitude'))
        distance_range = 100    # Distance in meters (configurable)
        reports_to_send = []
        for report in reports:
            if calculate_distance_between_coordinates(user_latitude, user_longitude, report.latitude, report.longitude) <= distance_range:
                reports_to_send.append(report)

        data = serializers.serialize('json', reports_to_send)
        return HttpResponse(data, content_type='application/json')

    @action(methods=['get'], detail=True, url_path='get-reports-by-type')
    def get_reports_by_state(self, request):
        report_state = request.data.get('report_state', '')
        reports = Incidencia.objects.filter(state=report_state)
        data = serializers.serialize('json', reports)
        return HttpResponse(data, content_type='application/json')

    @action(methods=['post'], detail=True, url_path='create-report')
    def create_report(self, request):
        cua = CustomUserAuthentication()
        request_user = cua.authenticate(request)

        new_report = Incidencia(
            report_date=request.data['report_date'],
            description=request.data['description'],
            image=request.data['image'],
            state=request.data['state'],
            latitude=request.data['latitude'],
            longitude=request.data['longitude'],
            author=request_user.email,
        )

        try:
            new_report.report_type = TipoIncidencia.objects.get(type=request.data['report_type'])
            new_report.save()
            return Response({'report': IncidenciaSerializer(new_report).data})
        except Exception as e:
            print(e)
            return Response({'error': 'Error al guardar incidencia'}, status=status.HTTP_400_BAD_REQUEST)

