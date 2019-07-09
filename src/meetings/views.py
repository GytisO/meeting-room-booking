from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import CreateRoomForm


def home_page(request):
    title = "Home"
    context = {"title": title}
    if request.user.is_authenticated:
        context = {"title": title, "my_list": [1, 2, 3, 4, 5, 6]}
    return render(request, "home.html", context)


# def about(request):
#     title = "about"
#     return render(request, "about.html", {"title": title})

def about(request):
    form = CreateRoomForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = CreateRoomForm()
    context = {
        "title": "Create new room",
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
