from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import requests
from API.models import Reservation
from .forms import CreateUserModelForm, LoginUserModelForm
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User


def user_create_view(request):
    template_name = 'user/create.html'
    form = CreateUserModelForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            data = request.POST.copy()
            response = requests.post(
                'http://localhost:8000/api/users/', data=data)
            # content = response.content
            return redirect('/')
    context = {
        "title": "Create new user",
        "form": form
    }
    return render(request, template_name, context)


@csrf_exempt
def user_login_view(request):
    template_name = 'user/login.html'
    form = LoginUserModelForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            data = request.POST.copy()
            print(data)
            response = requests.post(
                'http://localhost:8000/api/api-auth/login/', data=data
            )
            return redirect('/')
    context = {
        "title": "Login to your user",
        "form": form
    }
    return render(request, template_name, context)
