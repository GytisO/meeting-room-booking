from django.contrib.auth.models import User, Group
from django.db.models.fields import DateField, DurationField, TimeField
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import MeetingRoom, Reservation


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'password',
            'email',
            'groups',
            'id',
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }


class RoomSerializer(serializers.ModelSerializer):
    room_number = serializers.IntegerField()
    capacity = serializers.IntegerField()

    class Meta:
        model = MeetingRoom
        fields = [
            'url',
            'room_number',
            'capacity'
        ]


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'url',
            'room_number',
            'reservation_date',
            'reservation_time',
            'reservation_duration',
            'reservation_user',
            'id',
        ]
