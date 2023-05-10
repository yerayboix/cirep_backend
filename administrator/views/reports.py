from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cirep.helpers.functions import get_by_pk
from report.models import Incidencia, TipoIncidencia
from user.models import User


@login_required
def list_reports(request):
    reports = Incidencia.objects.all()
    context = {'reports': reports}
    return render(request, 'report/index.html', context)


@login_required
def list_user_reports(request, pk):
    us = User.objects.get(pk=pk)
    reports = Incidencia.objects.filter(author=us.email)
    context = {'reports': reports, 'us': us}
    return render(request, 'report/user_reports.html', context)


@login_required
def report_detail(request, pk):
    report = get_by_pk(Incidencia, pk)
    context = {'report': report, 'd_s_c': Incidencia.d_s_c}
    return render(request, 'report/detail.html', context)


@login_required
def report_update(request, pk):
    report = get_by_pk(Incidencia, pk)
    report_types = TipoIncidencia.objects.all()
    context = {'report': report, 'state_choices': Incidencia.STATE_CHOICES, 'report_types': report_types}
    if request.method == 'POST':
        state = request.POST['state']
        report_type = request.POST['report_type']

        try:
            report.report_type = TipoIncidencia.objects.get(type=report_type)
            report.state = state
            report.save()
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Ocurrió un error: {0}'.format(e))
            url = '/administrador/incidencias/detalles/{0}'.format(report.id)
            return redirect(url)
        url = '/administrador/incidencias/detalles/{0}'.format(report.id)
        messages.add_message(request, messages.SUCCESS, 'Incidencia actualizada con éxito.')
        return redirect(url)

    return render(request, 'report/update.html', context)
