from django.urls import path
from user import apis

urlpatterns = [
   path('register/',apis.RegisterApi.as_view(),name="register"),
   path('login/', apis.LoginApi.as_view(), name="login"),
   path('me/', apis.UserApi.as_view(), name="profile"),
   path('logout/', apis.LogoutApi.as_view(), name="logout")
]