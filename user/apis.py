from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import views, response, exceptions, permissions
import user.serializer as user_serializer
from . import services
from . import authentication
# Create your views here.
User = get_user_model()

class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data)

class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]#todo cambiar?
        password = request.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        token = services.create_token(user_id=user.id)

        return response.Response(data={"token":token})



class UserApi(views.APIView):
#el usuario tiene que estar autenticado
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):#creo que no es necesario
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        return response.Response()