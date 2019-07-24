from django.http import HttpResponse
from django.template.loader import get_template
from .forms import CreateRoomForm
from .forms import ReservationForm
from API.models import MeetingRoom
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def rooms(request):
    return HttpResponse("<h1>Room page</h1>")
