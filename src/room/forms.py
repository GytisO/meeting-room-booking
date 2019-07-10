from django import forms
from .models import MeetingRoom


class CreateRoomForm(forms.Form):
    room_number = forms.IntegerField()
    capacity = forms.IntegerField()


class CreateRoomModelForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['room_number', 'capacity']
