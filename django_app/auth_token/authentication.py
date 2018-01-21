from django.utils import timezone

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication as RestTokenAuthentication

from .models import Token


class TokenAuthentication(RestTokenAuthentication):
    model = Token

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if token.expired and token.expired < timezone.now():
            raise exceptions.AuthenticationFailed('Expired token.')
        return (user, token)
