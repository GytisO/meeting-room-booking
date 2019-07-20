from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import requests
from API.models import Reservation
from .forms import CreateReservationModelForm

from django.contrib.auth.models import User


def reservation_list_view(request):
    queryset = Reservation.objects.all()
    user_list = User.objects.all()
    title = "Reservations list"
    # queryset = MeetingRoom.objects.filter(room_number=201) - veikia kaip filtras
    template_name = 'reservation/list.html'
    context = {
        'title': title,
        'object_list': queryset,
        'user_list': user_list
    }
    return render(request, template_name, context)


@login_required
@api_view(['GET', 'POST'])
@csrf_exempt
def reservation_create_view(request):
    template_name = 'reservation/create.html'
    form = CreateReservationModelForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            data = request.POST.copy()
            user = request.user
            data.update({'reservation_user': int(user.id)})
            response = requests.post('http://localhost:8000/api/reservation/', data=data)
            content = response.content
            return redirect('/reservations/')


    # if form.is_valid():
    #     form.user = request.user
    #     user = str(form.user)
    #     data = request.POST.copy()
    #     print(form.user)
    #     print(data)

        # factory = APIRequestFactory()
        # factory.post('http://localhost:8000/api/reservations/', {'room_number': data['room_number'], 'reservation_date':
                                                                #  data['reservation_date'], 'reservation_time': data['reservation_time'], 'reservation_duration': data['reservation_duration'], 'reservation_user': user}, format = 'json')
        # return redirect('/reservations/')
        # print(factory.post)
    context={
        "title": "Create new reservation",
        "form": form
    }
    return render(request, template_name, context)


def reservation_detail_view(request, id, *room_number):
    title="Details of " + str(room_number) + " meeting room"
    obj=get_object_or_404(Reservation, id = id)
    template_name='reservation/detail.html'
    context={
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)


@login_required
def reservation_update_view(request, *room_number, id):
    title="Updating " + str(room_number) + " room reservation"
    obj=get_object_or_404(Reservation, id = id)
    form=CreateReservationModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/reservations')
    template_name='reservation/create.html'
    context={
        'title': title,
        'object': obj,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def reservation_delete_view(request, *room_number, id):
    title="Deleting " + str(room_number) + " meeting room"
    obj=get_object_or_404(Reservation, id = id)
    template_name='reservation/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/reservations')
    context={
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)
