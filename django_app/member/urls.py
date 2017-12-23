from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url('^token-auth/$', obtain_jwt_token, name="get_token"),
    url('^token-refresh/$', refresh_jwt_token, name="refresh_token"),
]
