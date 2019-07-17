from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import requests
from rest_framework.test import APIClient

# Create your views here.
# from .models import Reservation
from API.models import Reservation

from .forms import CreateReservationModelForm


def reservation_list_view(request):
    queryset = Reservation.objects.all()
    title = "Reservations list"
    # queryset = MeetingRoom.objects.filter(room_number=201) - veikia kaip filtras
    template_name = 'reservation/list.html'
    context = {
        'title': title,
        'object_list': queryset
    }
    return render(request, template_name, context)


@login_required
def reservation_create_view(request):
    template_name = 'reservation/create.html'
    form = CreateReservationModelForm(request.POST or None)
    if form.is_valid():
        form.user = request.user
        data = request.POST.copy()
        client = APIClient()
        client.post('http://localhost:8000/api/reservation/', {'r_number': data.get('id_r_number'), 'r_date': data.get(
            'id_r_date'), 'r_time': data.get('id_r_time'), 'r_duration': data.get('id_r_duration')}, format='json')
        # requests.post('http://localhost:8000/api/reservation/', data={'r_number': data.get('id_r_number'), 'r_date': data.get(
        #     'id_r_date'), 'r_time': data.get('id_r_time'), 'r_duration': data.get('id_r_duration')})
        # form.save()
        # form = ReservationForm()
        return redirect('/reservations/')
    context = {
        "title": "Create new reservation",
        "form": form
    }
    return render(request, template_name, context)


def reservation_detail_view(request, r_number):
    title = "Details of " + str(r_number) + " meeting room"
    obj = get_object_or_404(Reservation, r_number=r_number)
    template_name = 'reservation/detail.html'
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)


@login_required
def reservation_update_view(request, r_number):
    title = "Updating " + str(r_number) + " room reservation"
    obj = get_object_or_404(Reservation, r_number=r_number)
    form = CreateReservationModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/reservations')
    template_name = 'reservation/create.html'
    context = {
        'title': title,
        'object': obj,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def reservation_delete_view(request, r_number):
    title = "Deleting " + str(r_number) + " meeting room"
    obj = get_object_or_404(Reservation, r_number=r_number)
    template_name = 'reservation/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/reservations')
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)
