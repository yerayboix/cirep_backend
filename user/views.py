from django.db import models
from rest_framework import serializers, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # obtén los datos de la petición
        data = request.data.copy()

        # crea y guarda el objeto Usuario con los datos actualizados
        usuario = User(
            email=data.get('email', ''),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
        )

        # devuelve la respuesta con el objeto Usuario creado
        usuario.set_password(data['password'])
        usuario.save()
        serializer = self.get_serializer(usuario)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        password = request.data.get('password')
        if password:
            user.set_password(password)
            user.save()
            return Response({'detail': 'Contraseña actualizada.'})
        else:
            return Response({'detail': 'Debe proporcionar una contraseña.'}, status=status.HTTP_400_BAD_REQUEST)