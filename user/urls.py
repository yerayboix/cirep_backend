from django.urls import path
from user import apis

urlpatterns = [
   path('register/',apis.RegisterApi.as_view(),name="register")
]