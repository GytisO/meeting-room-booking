from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from API.models import MeetingRoom
from .forms import CreateRoomModelForm


def room_list_view(request):
    queryset = MeetingRoom.objects.all()
    print(queryset)
    title = "Meeting room list"
    template_name = 'room/list.html'
    context = {
        'title': title,
        'object_list': queryset
    }
    return render(request, template_name, context)


@login_required
def room_create_view(request):
    template_name = 'room/create.html'
    form = CreateRoomModelForm(request.POST or None)
    if form.is_valid():

        form.user = request.user
        form.save()
        form = CreateRoomModelForm()
        return redirect('/rooms')
    context = {
        "title": "Create new room",
        "form": form
    }
    return render(request, template_name, context)


def room_detail_view(request, room_number):
    title = "Details of " + str(room_number) + " meeting room"
    obj = get_object_or_404(MeetingRoom, room_number=room_number)
    template_name = 'room/detail.html'
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)


@login_required
def room_update_view(request, room_number):
    title = "Updating " + str(room_number) + " meeting room"
    obj = get_object_or_404(MeetingRoom, room_number=room_number)
    form = CreateRoomModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/rooms')
    template_name = 'room/create.html'
    context = {
        'title': title,
        'object': obj,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def room_delete_view(request, room_number):
    title = "Deleting " + str(room_number) + " meeting room"
    obj = get_object_or_404(MeetingRoom, room_number=room_number)
    template_name = 'room/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/rooms')
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)
