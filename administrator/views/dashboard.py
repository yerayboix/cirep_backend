from django.shortcuts import render

from cirep.helpers.functions import clasificar_por_mes
from report.models import Incidencia
from user.models import User


def render_dashboard(request):
    incidencias = Incidencia.objects.all()
    incidencias_arregladas = Incidencia.objects.filter(state='A')
    incidencias_pendientes = Incidencia.objects.filter(state='PR')
    incidencias_en_proceso = Incidencia.objects.filter(state='P')
    incidencias_descartadas = Incidencia.objects.filter(state='D')
    users = User.objects.all()

    fechas = []
    for incidencia in incidencias:
        fechas.append(incidencia.report_date)

    fechas_clasificadas = clasificar_por_mes(fechas)

    context = {'incidencias': incidencias, 'incidencias_arregladas': incidencias_arregladas,
               'incidencias_pendientes': incidencias_pendientes, 'incidencias_en_proceso': incidencias_en_proceso,
               'users': users, 'incidencias_descartadas': incidencias_descartadas,
               'fechas_clasificadas': fechas_clasificadas}

    return render(request, 'dashboard.html', context)