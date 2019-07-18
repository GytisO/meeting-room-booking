from django.contrib.auth.models import User, Group
from django.db.models.fields import DateField, DurationField, TimeField
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from room.models import MeetingRoom
# from reservation.models import Reservation

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

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


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

    # room_number = serializers.ChoiceField(MeetingRoom)
    # reservation_date = serializers.DateField()
    # reservation_time = serializers.TimeField()
    # reservation_duration = DurationField()

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
