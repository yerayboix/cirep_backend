from django.urls import path, include
from rest_framework import routers

from report.views import IncidenciaViewSet

urlpatterns = [
    path('get_all_reports/', IncidenciaViewSet.as_view({'get': 'get_all_reports'}), name='get-all-reports'),
    path('get_user_reports/', IncidenciaViewSet.as_view({'get': 'get_user_reports'}), name='get-user-reports'),
    path('create_report/', IncidenciaViewSet.as_view({'post': 'create_report'}), name='create-report'),
]