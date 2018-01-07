from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_token.models import Token
from .models import User
from .serializers import SimpleUserSerializer, UserCreateSerializer, LoginSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    pagination_class = LimitOffsetPagination

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


class LoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        keep_login = serializer.validated_data.get('keep_login', False)
        user = authenticate(email=email, password=password)
        if user is None:
            raise ValidationError({"error": "아이디 혹은 비밀번호를 확인하셍ㅛ"})
        user.update_last_login()
        token, created = Token.objects.get_or_create(user=user)
        if created:  # Token이 새로 생성 된 경우
            pass
        elif not created and token.is_available():  # 기존에 있는 토큰이며, 사용 가능한 토큰인 경우 만료시간 갱신
            token.refresh()
        else:  # 기존에 있던 토큰이며, Expired 된 경우 재생성
            token = Token.regenerate(user=user)
        if keep_login:  # 로그인 유지가 True인 경우
            token.expired = None
            token.save()
        user.update_last_login()
        return Response(data={"token": token.key, "expired_date": token.expired}, status=status.HTTP_200_OK)
