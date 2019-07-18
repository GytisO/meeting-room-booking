from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class MeetingRoom(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    room_number = models.IntegerField(unique=True, blank=False)
    capacity = models.IntegerField(blank=False)
    # models.One

    def __str__(self):
        return str(self.room_number)

    def get_absolute_url(self):
        return reverse('room-details', kwargs={'room_number': self.room_number})


class Reservation(models.Model):
    id: models.AutoField(auto_created=True, primary_key=True)
    reservation_user = models.ForeignKey(User, default=1, null=True,
                                         on_delete=models.SET_NULL)
    room_number = models.ForeignKey(
        MeetingRoom, on_delete=models.SET_NULL, null=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_duration = models.DurationField()

    def __str__(self):
        return self.room_number

    def get_absolute_url(self):
        return reverse('reservation-details', kwargs={'id': self.id})
