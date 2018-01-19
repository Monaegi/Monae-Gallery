from datetime import timedelta

from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token as RestToken


class Token(RestToken):
    expired = models.DateTimeField(default=timezone.now() + timedelta(days=7), null=True)

    def is_available(self):
        return self.expired is None or self.expired > timezone.now()

    @classmethod
    def regenerate(cls, user):
        cls.objects.get(user=user).delete()
        token = cls.objects.create(user=user)
        return token

    def refresh(self):
        self.expired = timezone.now() + timedelta(days=7)
        self.save()

    def keep_login(self):
        self.expired = None
        self.save()
