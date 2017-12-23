from django.db import models
from member.models import User


class Schedules(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    scheduled_date_start = models.DateTimeField()
    scheduled_date_end = models.DateTimeField()

    user = models.ForeignKey(User)
    event_name = models.CharField(max_length=100)
    event_detail = models.TextField()
    room = models.CharField(max_length=50)
