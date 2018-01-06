from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'phone_number',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, max_length=16)
    password2 = serializers.CharField(write_only=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'phone_number',
            'password1',
            'password2',
        )

    def validate(self, data):
        if not data['password1'] == data['password2']:
            raise ValidationError("패스워드 확인이 틀렸습니다.")
        data.pop('password2', None)
        data['password'] = data.pop('password1')
        return data

    def save(self, **kwargs):
        super().save(**kwargs)
        self.instance.set_password(self.validated_data['password'])
        self.instance.save()
        return self.instance
