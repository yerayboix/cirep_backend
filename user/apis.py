from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import views, response, exceptions, permissions
import user.serializer as user_serializer
from user import services

# Create your views here.
User = get_user_model()

class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data)

