from django import forms


class CreateRoomForm(forms.Form):
    room_number = forms.IntegerField()
    capacity = forms.IntegerField()


class ReservationForm(forms.Form):
    reservation_date = forms.DateField(
        widget=forms.SelectDateWidget(empty_label="Not set", months=None)
    )
