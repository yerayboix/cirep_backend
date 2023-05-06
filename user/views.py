
from django.db import models
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.authentication import CustomUserAuthentication
from user.models import User
from user.serializer import UserSerializer
from . import services


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        # obtén los datos de la petición
        data = request.data.copy()

        # crea y guarda el objeto Usuario con los datos actualizados
        usuario = User(
            email=data.get('email', ''),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            phone_number=data.get('phone_number', ''),
            city=data.get('city', '')
        )

        # devuelve la respuesta con el objeto Usuario creado
        usuario.set_password(data['password'])
        try:
            usuario.save()
        except Exception as e:
            print(e)
            return Response({'error': 'Usuario ya registrado'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(usuario)
        headers = self.get_success_headers(serializer.data)
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        token = services.create_token(user_id=usuario.id)
        response.data['token'] = token
        return response

    @action(detail=True, methods=['post'])
    def login(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(raw_password=password):
            return Response({'error': 'Credenciales no validos'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(user)
        headers = self.get_success_headers(serializer.data)

        token = services.create_token(user_id=user.id)

        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        response.data['token'] = token

        return response

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        cua = CustomUserAuthentication()

        request_user = cua.authenticate(request)
        if request_user is None:
            return Response({'error': 'Necesitas iniciar sesión'},
                            status=status.HTTP_401_UNAUTHORIZED)
        # verificamos que el usuario que quiere cambiar la contraseña sea el mismo que al que se le quiere cambiar
        if request_user.id != user.id:
            return Response({'error': 'No tienes permisos para cambiar la contraseña de este usuario.'}, status=status.HTTP_401_UNAUTHORIZED)
        password = request.data.get('password')
        if password:
            user.set_password(password)
            user.save()
            return Response({'detail': 'Contraseña actualizada.'})
        else:
            return Response({'detail': 'Debe proporcionar una contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='modify-profile')
    def modify_profile(self, request, email):
        user = User.objects.get(email=email)
        cua = CustomUserAuthentication()

        request_user = cua.authenticate(request)
        if request_user is None:
            return Response({'error': 'Necesitas iniciar sesión'},
                            status=status.HTTP_401_UNAUTHORIZED)
        # verificamos que el usuario que quiere modificar su perfil sea el mismo que al que se le quiere cambiar
        if request_user.id != user.id:
            return Response({'error': 'No tienes permisos para modificar este usuario.'},
                            status=status.HTTP_401_UNAUTHORIZED)
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        city = request.data.get('city')
        password = request.data.get('password')

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if phone_number:
            user.phone_number = phone_number
        if city:
            user.city = city
        if password:
            user.set_password(password)
            user.save()

        try:
            user.save()
            return Response({'detail': 'Perfil actualizado.'})
        except Exception as e:
            print(e)
            return Response({'error': 'Error al modificar perfil.'}, status=status.HTTP_400_BAD_REQUEST)
