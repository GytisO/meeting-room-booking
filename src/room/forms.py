from django import forms
# from .models import MeetingRoom
from API.models import MeetingRoom


class CreateRoomForm(forms.Form):
    room_number = forms.ModelChoiceField(queryset=MeetingRoom.objects.all())
    capacity = forms.IntegerField()


class CreateRoomModelForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['room_number', 'capacity']
