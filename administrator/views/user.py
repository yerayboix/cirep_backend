from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
