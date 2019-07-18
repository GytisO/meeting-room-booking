from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
# from .models import MeetingRoom
from API.models import MeetingRoom
from .forms import CreateRoomModelForm


# def meeting_room_detail_page(request, room_number):
#     obj = get_object_or_404(MeetingRoom, room_number=room_number)
#     template_name = 'meeting_room_detail_page.html'
#     context = {"object": obj}
#     return render(request, template_name, context)


# def meeting_room_list(request):
#     queryset = MeetingRoom.objects.all()
#     template_name = 'meeting_room_list.html'
#     context = {
#         'object_list': queryset
#     }
#     return render(request, template_name, context)


def room_list_view(request):
    queryset = MeetingRoom.objects.all()
    title = "Meeting room list"
    # queryset = MeetingRoom.objects.filter(room_number=201) - veikia kaip filtras
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
        # obj = MeetingRoom.objects.create(**form.cleaned_data)
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
    # redirect('room/list.html')
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
