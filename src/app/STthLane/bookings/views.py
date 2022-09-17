from django.shortcuts import render, redirect
from bookings.forms.new_booking_form import CreateBookingForm

# Create your views here.
def add_bookings(request):
    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-index')
    else:
        form = CreateBookingForm()
    return render(request, 'bookings/add_booking.html', {'form': form})
