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
    # reservation_number = models.AutoField(primary_key=True)
    r_user = models.ForeignKey(User, default=1, null=True,
                               on_delete=models.SET_NULL)
    r_number = models.ForeignKey(
        MeetingRoom, on_delete=models.SET_NULL, null=True)
    r_date = models.DateField()
    r_time = models.TimeField()
    r_duration = models.DurationField()

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse('reservation-details', kwargs={'r_number': self.r_number})
