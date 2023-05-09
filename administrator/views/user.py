from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cirep.helpers.functions import get_by_pk
from user.models import User


@login_required
def list_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user/index.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def desactivate_user(request, pk):
    user = get_by_pk(User, pk)
    user.is_active = False
    user.save()
    return redirect('/administrador/usuarios/listado')


@login_required
def activate_user(request, pk):
    user = get_by_pk(User, pk)
    user.is_active = True
    user.save()
    return redirect('/administrador/usuarios/listado')
