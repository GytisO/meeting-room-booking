from django.contrib.auth.models import User, Group
from django.db.models.fields import DateField, DurationField, TimeField
from rest_framework import serializers
from django.contrib.auth import get_user_model
from room.models import MeetingRoom
from reservation.models import Reservation


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
            'room_number',
            'capacity'
        ]


class ReservationSerializer(serializers.ModelSerializer):
    r_number = serializers.IntegerField()
    r_date = serializers.DateField()
    r_time = serializers.TimeField()
    r_duration = DurationField()

    class Meta:
        model = Reservation
        fields = [
            'r_number',
            'r_date',
            'r_time',
            'r_duration',
            'r_user',
        ]
