from django.db import models
from django.urls import reverse


# Create your models here.


class MeetingRoom(models.Model):
    room_number = models.IntegerField(unique=True, blank=False)
    capacity = models.IntegerField(blank=False)

    def get_absolute_url(self):
        return reverse('room-details', kwargs={'room_number': self.room_number})
