from django.contrib.auth.models import User, Group
from room.models import MeetingRoom
from reservation.models import Reservation
from rest_framework import viewsets
from .serializers import UserSerializer, ReservationSerializer, RoomSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = RoomSerializer
