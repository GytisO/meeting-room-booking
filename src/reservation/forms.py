from django import forms
# from .models import Reservation
from API.models import Reservation


class CreateReservationForm(forms.Form):
    # r_number = forms.IntegerField()
    r_number = forms.ModelChoiceField(queryset=Reservation.objects.all())
    r_date = forms.DateField()
    r_time = forms.TimeField()
    r_duration = forms.DurationField()


class CreateReservationModelForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'r_number',
            'r_date',
            'r_time',
            'r_duration'
        ]
