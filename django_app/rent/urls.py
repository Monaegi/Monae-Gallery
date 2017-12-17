from django.conf.urls import url

from rent.views import *

app_name = 'rent'
urlpatterns = [
    url(r'^scheduler/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', CalendarView.as_view(), name='calendar'),
]