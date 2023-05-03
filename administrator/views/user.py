from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user.models import User


@login_required
def list_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user/index.html', context)
