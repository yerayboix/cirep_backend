from django.urls import path, include
from rest_framework import routers

from user.views import UserViewSet

urlpatterns = [
    path('<pk>/change_password/', UserViewSet.as_view({'post': 'change_password'}), name='user-change-password'),
    path('create/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('modificar_perfil/<email>/', UserViewSet.as_view({'post': 'modify_profile'}), name='modify_profile'),
]