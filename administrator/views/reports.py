from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cirep.helpers.functions import get_by_pk, decodify_image
from report.models import Incidencia, TipoIncidencia, IncidenciaPorNotificar, IncidenciaDesacreditada
from user.models import User


@login_required
def list_reports(request):
    reports = Incidencia.objects.all()
    reports_images = []
    request.session['origen'] = request.build_absolute_uri()
    for report in reports:
        image = report.image
        reports_images.append((image, report))
    context = {'reports_images': reports_images}
    return render(request, 'report/index.html', context)


@login_required
def list_discredit_reports(request):
    reports = IncidenciaDesacreditada.objects.all()
    context = {'reports': reports}
    return render(request, 'report/discredit_reports.html', context)


@login_required
def list_user_reports(request, pk):
    us = User.objects.get(pk=pk)
    reports = Incidencia.objects.filter(author=us.email)
    request.session['origen'] = request.build_absolute_uri()
    context = {'reports': reports, 'us': us}
    return render(request, 'report/user_reports.html', context)


@login_required
def report_detail(request, pk):
    report = get_by_pk(Incidencia, pk)
    origen = request.GET.get('origen')
    context = {'report': report, 'd_s_c': Incidencia.d_s_c, 'url_origen': origen}
    return render(request, 'report/detail.html', context)


@login_required
def report_update(request, pk):
    report = get_by_pk(Incidencia, pk)
    report_types = TipoIncidencia.objects.all()
    origen = request.GET.get('origen')
    print(origen)
    context = {'report': report, 'state_choices': Incidencia.STATE_CHOICES, 'report_types': report_types, 'url_origen': origen}
    if request.method == 'POST':
        state = request.POST['state']
        report_type = request.POST['report_type']

        try:
            if state != report.state:
                try:
                    new_incidencia_por_notificar = IncidenciaPorNotificar(
                        incidencia=report
                    )
                    new_incidencia_por_notificar.save()
                except Exception as e:
                    print(e)
            report.report_type = TipoIncidencia.objects.get(type=report_type)
            report.state = state
            report.save()
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Ocurrió un error: {0}'.format(e))
            url = '/administrador/incidencias/detalles/{0}?origen={1}'.format(report.id, origen)
            return redirect(request.META['HTTP_REFERER'])

        url = '/administrador/incidencias/detalles/{0}?origen={1}'.format(report.id, origen)
        messages.add_message(request, messages.SUCCESS, 'Incidencia actualizada con éxito.')
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'report/update.html', context)


@login_required
def revise_report(request, pk):
    report = get_by_pk(Incidencia, pk)
    report_types = TipoIncidencia.objects.all()
    context = {'report': report, 'state_choices': Incidencia.STATE_CHOICES, 'report_types': report_types}
    if request.method == 'POST':
        state = request.POST['state']

        try:
            if state != report.state:
                try:
                    new_incidencia_por_notificar = IncidenciaPorNotificar(
                        incidencia=report
                    )
                    new_incidencia_por_notificar.save()
                except Exception as e:
                    print(e)
            report.state = state
            report.save()
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Ocurrió un error: {0}'.format(e))
            url = '/administrador/incidencias/desacreditadas/'
            return redirect(url)
        url = '/administrador/incidencias/desacreditadas/'
        messages.add_message(request, messages.SUCCESS, 'Incidencia actualizada con éxito.')
        return redirect(url)

    return render(request, 'report/revise_report.html', context)