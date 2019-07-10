from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.

User = settings.AUTH_USER_MODEL


class MeetingRoom(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    room_number = models.IntegerField(unique=True, blank=False)
    capacity = models.IntegerField(blank=False)

    def get_absolute_url(self):
        return reverse('room-details', kwargs={'room_number': self.room_number})
