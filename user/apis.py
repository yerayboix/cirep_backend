from django.shortcuts import render
from django.contrib.auth import get_user_model
from requests import Response
from rest_framework import views, response, exceptions, permissions, status
import user.serializer as user_serializer
from . import services
from . import authentication
from .services import user_email_selector

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

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, httponly=True)

        return resp



class UserApi(views.APIView):
#el usuario tiene que estar autenticado
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "so long farewell"}

        return resp

class ChangePasswordApi(views.APIView):
#el usuario tiene que estar autenticado
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request):
        data=request.data
        password_serializer = user_serializer.ChangePasswordSerializer(data=data,context={'request': request})
        password_serializer.is_valid()
        password_serializer.validate(data)
        password_serializer.validate_old_password(request.data['old_password'])
        user_model = user_email_selector(request.user)

        password_serializer.update(instance=user_model,validated_data=data)
        resp = response.Response()
        resp.data = {"message": "password updated"}

        return resp



