from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import MeetingRoom


def meeting_room_detail_page(request, room_number):
    obj = get_object_or_404(MeetingRoom, room_number=room_number)
    template_name = 'meeting_room_detail_page.html'
    context = {"object": obj}
    return render(request, template_name, context)


def meeting_room_list(request):
    queryset = MeetingRoom.objects.all()
    template_name = 'meeting_room_list.html'
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


def room_list_view(request):
    template_name = 'room_list.html'
    context = {
        'object_list': []
    }
    return render(request, template_name, context)


def room_create_view(request):
    # use form
    template_name = 'room_create.html'
    context = {
        'form': None
    }
    return render(request, template_name, context)


def room_detail_view(request):
    obj = get_object_or_404(MeetingRoom, room_number=room_number)
    template_name = 'room_detail.html'
    context = {
        'object': obj
    }
    return render(request, template_name, context)


def room_update_view(request):
    obj = get_object_or_404(MeetingRoom, room_number=room_number)
    template_name = 'room_update.html'
    context = {
        'object': obj,
        'form': None,
    }
    return render(request, template_name, context)


def room_delete_view(request):
    obj = get_object_or_404(MeetingRoom, room_number=room_number)
    template_name = 'room_delete.html'
    context = {
        'object': obj
    }
    return render(request, template_name, context)
