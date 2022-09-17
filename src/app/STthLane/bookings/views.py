from django.shortcuts import render, redirect
from bookings.forms.new_booking_form import CreateBookingForm
from django.contrib import messages
from bookings.models import bookings, lanes, booking_time_slots, booked_lanes
from datetime import datetime
import math

# Create your views here.
def add_bookings(request):
    """
    Is used to add a new booking to the database
    """
    all_time_slots = booking_time_slots.objects.all()
    if request.method == 'POST':
        form = CreateBookingForm(request.POST)

        if form.is_valid():
            if int(request.POST.get('player_amount')) > 0:
                req_date = datetime.strptime(request.POST['date'], "%Y-%m-%d")
                req_time = all_time_slots.get(id=request.POST['time_slot'])
                request_datetime = datetime.combine(req_date, req_time.start_time) # The datetime of the booking

                if request_datetime > datetime.now(): # If the booking is in the future
                    lanes_filter = booked_lanes.objects.filter(date=request.POST['date'], time_slot=req_time) # Get all lanes that are booked on the same date and time slot
                    free_lanes = lanes.objects.exclude(lane_nr__in=lanes_filter.values_list('lane_nr')) # Filter out all lanes that are booked on the same date and time slot
                    needed_lanes = math.ceil(int(request.POST['player_amount']) / 6) # Calculates how many lanes are needed

                    if needed_lanes <= len(free_lanes):
                        form.save(commit=False)
                        form.instance.time_slot = req_time
                        form.save()
                        for i in range(needed_lanes):
                            booked_lane = booked_lanes()
                            booked_lane.booking = form.instance
                            booked_lane.lane_nr = free_lanes[i]
                            booked_lane.time_slot = req_time
                            booked_lane.date = request.POST['date']
                            booked_lane.save()

                        messages.success(request, 'The booking was successfully created! '+ str(needed_lanes) + ' lanes were booked.')
                        return redirect('add-booking')
                    else:
                        messages.error(request, 'There are not enough lanes available for this booking')
                else:
                    messages.error(request, 'The date you entered is in the past')
            else:
                messages.error(request, 'The amount of players must be at least 1')
        messages.error(request, 'Please fill in all fields')
    else:
        form = CreateBookingForm()
    return render(request, 'bookings/add_booking.html', {'form': form})
