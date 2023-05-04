from django.urls import path, include
from rest_framework import routers

from administrator.views.reports import list_reports
from administrator.views.user import list_users, logout_view, activate_user, desactivate_user

urlpatterns = [
    # Usuarios
    path('usuarios/listado', list_users, name='list_users'),
    path('usuarios/logout', logout_view, name='logout_view'),
    path('usuarios/activar/<pk>', activate_user, name='activate_user'),
    path('usuarios/desactivar/<pk>', desactivate_user, name='desactivate_user'),
    # Incidencias
    path('incidencias/listado', list_reports, name='list_reports'),
]