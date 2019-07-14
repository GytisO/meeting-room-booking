from django.http import HttpResponse
from django.template.loader import get_template
from .forms import CreateRoomForm
from .forms import ReservationForm
from room.models import MeetingRoom
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def home_page(request):
    objectlist = MeetingRoom.objects.all()
    reservation_date = ReservationForm(request.POST or None)
    if reservation_date.is_valid():
        reservation_date.user = request.user
        reservation_date = ReservationForm()
    title = "Home"
    context = {"title": "You have to be logged in"}
    if request.user.is_authenticated:
        context = {"title": title, "my_list": [
            1, 2, 3, 4, 5, 6], "objectlist": objectlist, "reservation_date": reservation_date}
    return render(request, "home.html", context)


# def about(request):
#     title = "about"
#     return render(request, "about.html", {"title": title})

@login_required
def about(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.user = request.user
        form.save()
        # form = ReservationForm()
        return redirect('/')
    context = {
        "title": "Create new reservation",
        "form": form
    }
    return render(request, "about.html", context)


def rooms(request):
    return HttpResponse("<h1>Room page</h1>")


def example(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
