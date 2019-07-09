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
from django.urls import path
from .views import room_detail_view, room_list_view, room_update_view, room_delete_view, room_create_view


urlpatterns = [
    path('', room_list_view, name='room-list'),
    path('<int:room_number>/', room_detail_view, name='room-details'),
    path('<int:room_number>/update/',
         room_update_view, name='room-update'),
    path('<int:room_number>/delete/',
         room_delete_view, name='room-delete'),
    path('create/', room_create_view, name='room-create'),
]
