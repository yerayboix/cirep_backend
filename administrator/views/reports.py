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

