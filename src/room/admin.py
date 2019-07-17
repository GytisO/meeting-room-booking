from django.contrib import admin

# Register your models here.

# from .models import MeetingRoom

from API.models import MeetingRoom

admin.site.register(MeetingRoom)
