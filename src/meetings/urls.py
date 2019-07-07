"""meetings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from .views import (home_page, rooms, about, example)
from room.views import meeting_room_detail_page, meeting_room_list


urlpatterns = [
    path('', home_page),
    re_path(r'example?/$', example),
    # re_path(r'^rooms?/$', rooms),
    re_path(r'^about/$', about),
    path('meeting-admin/', admin.site.urls),
    path('rooms/', meeting_room_list, name='room-list'),
    path('rooms/<int:room_number>/', meeting_room_detail_page, name='room-details'),
]
