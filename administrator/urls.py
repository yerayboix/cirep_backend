from django.urls import path, include
from rest_framework import routers

from administrator.views.dashboard import render_dashboard
from administrator.views.reports import list_reports, list_user_reports, report_detail, report_update, \
    list_discredit_reports, revise_report
from administrator.views.user import list_users, logout_view, activate_user, desactivate_user, user_details

urlpatterns = [
    # Usuarios
    path('usuarios/listado', list_users, name='list_users'),
    path('usuarios/logout', logout_view, name='logout_view'),
    path('usuarios/activar/<pk>', activate_user, name='activate_user'),
    path('usuarios/desactivar/<pk>', desactivate_user, name='desactivate_user'),
    path('usuarios/detalles/<pk>', user_details, name='user_details'),
    # Incidencias
    path('incidencias/listado', list_reports, name='list_reports'),
    path('incidencias/listado/usuario/<pk>', list_user_reports, name='list_user_reports'),
    path('incidencias/detalles/<pk>', report_detail, name='report_detail'),
    path('incidencias/editar/<pk>', report_update, name='report_update'),
    path('incidencias/desacreditadas/', list_discredit_reports, name='list_discredit_reports'),
    path('incidencias/revisar/<pk>', revise_report, name='revise_report'),
    # Dashboard
    path('dashboard/', render_dashboard, name='render_dashboard'),
]