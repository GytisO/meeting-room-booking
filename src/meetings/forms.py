from django import forms


class CreateRoomForm(forms.Form):
    room_number = forms.IntegerField()
    capacity = forms.IntegerField()
