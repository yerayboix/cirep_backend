from rest_framework import serializers
from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    age = serializers.IntegerField()
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)
