from rest_framework import generics
# Create your views here.
from rest_framework.filters import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import SimpleUserSerializer, UserCreateSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SimpleUserSerializer
        elif self.request.method == "POST":
            return UserCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAdminUser(), ]
        else:
            return []
