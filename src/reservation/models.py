from django.conf import settings
from django.db import models
from django.urls import reverse
from room.models import MeetingRoom


# Create your models here.

User = settings.AUTH_USER_MODEL
RoomNumber = MeetingRoom.room_number


class Reservation(models.Model):
    r_user = models.ForeignKey(User, default=1, null=True,
                               on_delete=models.SET_NULL)
    r_number = models.IntegerField()
    # r_number = models.OneToOneField(
    #     MeetingRoom, on_delete=models.SET_NULL, null=True)
    r_date = models.DateField()
    r_time = models.TimeField()
    r_duration = models.DurationField()
    # models.One

    def get_absolute_url(self):
        return reverse('reservation-details', kwargs={'r_number': self.r_number})
