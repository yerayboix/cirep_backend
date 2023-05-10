from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cirep.helpers.functions import get_by_pk
from report.models import Incidencia
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
