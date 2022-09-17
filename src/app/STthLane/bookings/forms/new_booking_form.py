from django.forms import ModelForm, widgets
from django import forms
from bookings.models import bookings, lanes, booking_time_slots

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateBookingForm(ModelForm):
    class Meta:
        TIME_SLOT_CHOICES = [
            ('8:00 - 9:00', '8:00 - 9:00'), ('9:00 - 10:00', '9:00 - 10:00'), ('10:00 - 11:00', '10:00 - 11:00'),
            ('11:00 - 12:00', '11:00 - 12:00'), ('12:00 - 13:00', '12:00 - 13:00'), ('13:00 - 14:00', '13:00 - 14:00'),
            ('14:00 - 15:00', '14:00 - 15:00'), ('15:00 - 16:00', '15:00 - 16:00'), ('16:00 - 17:00', '16:00 - 17:00'),
            ('17:00 - 18:00', '17:00 - 18:00'), ('18:00 - 19:00', '18:00 - 19:00'), ('19:00 - 20:00', '19:00 - 20:00'),
            ('20:00 - 21:00', '20:00 - 21:00'), ('21:00 - 22:00', '21:00 - 22:00'), ('22:00 - 23:00', '22:00 - 23:00'),
            ('23:00 - 24:00', '23:00 - 24:00')
        ]
        model = bookings
        exclude = {
            'id',
            'lane_nr',
            'payed',
        }
        widgets = {
        'booker_phone': widgets.TextInput(attrs={'class': 'form-control'}),
        'date': DateInput(),
        'time_slot': widgets.Select(attrs={'class': 'form-control'}, choices=TIME_SLOT_CHOICES),
        }