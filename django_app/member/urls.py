from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UserListCreateView.as_view(), name='list_create'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
]
