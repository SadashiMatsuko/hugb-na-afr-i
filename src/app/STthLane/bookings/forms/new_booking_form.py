from django.forms import ModelForm, widgets
from django import forms
from bookings.models import bookings, lanes, booking_time_slots

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateBookingForm(ModelForm):
    class Meta:
        model = bookings
        exclude = {
            'id',
            'time_slot',
        }
        widgets = {
        'booker_phone': widgets.TextInput(attrs={'class': 'form-control'}),
        'date': DateInput(),
        'player_amount': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
    time_slot = forms.ModelChoiceField(queryset=booking_time_slots.objects.all().order_by("id"), widget=forms.Select(attrs={'class': 'form-control'}))
