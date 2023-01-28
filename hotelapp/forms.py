from django import forms
from django.forms import SelectDateWidget
from hotelapp.models import Hotel, Room, Reservations

DATE_INPUT_FORMATS = ['%d/%m/%Y']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['user', 'name']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'capacity', 'guests', 'is_taken']


class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ['start', 'end']
        widgets = {
            'start': SelectDateWidget(attrs={}, years=range(2023, 2024), ),
            'end': SelectDateWidget(attrs={}),
        }




