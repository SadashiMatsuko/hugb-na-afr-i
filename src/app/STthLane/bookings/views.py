from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bookings.forms.new_booking_form import CreateBookingForm
from django.contrib import messages
from bookings.models import bookings, lanes, booking_time_slots, booked_lanes
from datetime import datetime
import math

# Create your views here.

@login_required
def index(request):
    """
    Is used to show all bookings in the database
    """
    return render(request, 'bookings/index.html', {'bookings': bookings.objects.all().order_by('date'), 'lanes': booked_lanes.objects.all()})


@login_required
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
                        add_lanes_to_booking(request, form, needed_lanes, free_lanes, req_time)
                        messages.success(request, 'The booking was successfully created! '+ str(needed_lanes) + ' lanes were booked.')
                        return redirect('bookings-index')
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

@login_required
def remove_booking(request, booking_id):
    """
    Is used to remove a specific booking
    """
    if booking_id in bookings.objects.values_list('id', flat=True):
        lanes = booked_lanes.objects.filter(booking_id=booking_id)
        lanes.delete()
        booking = bookings.objects.get(pk=booking_id)
        booking.delete()
        messages.success(request, 'The booking was successfully removed!')
    else:
        messages.error(request, 'The booking you tried to remove does not exist')
    return redirect('bookings-index')

@login_required
def edit_booking(request, booking_id):
    """
    Is used to edit a specific booking
    """
    booking = get_object_or_404(bookings, pk=booking_id)
    if request.method == 'POST':
        form = CreateBookingForm(instance=booking, data=request.POST)
        if form.is_valid():
            if int(request.POST.get('player_amount')) > 0:
                req_date = datetime.strptime(request.POST['date'], "%Y-%m-%d")
                req_time = booking_time_slots.objects.get(id=request.POST['time_slot'])
                request_datetime = datetime.combine(req_date, req_time.start_time)

                if request_datetime > datetime.now():
                    lanes_filter = booked_lanes.objects.filter(date=request.POST['date'], time_slot=req_time).exclude(booking_id=booking_id)
                    free_lanes = lanes.objects.exclude(lane_nr__in=lanes_filter.values_list('lane_nr'))
                    needed_lanes = math.ceil(int(request.POST['player_amount']) / 6)

                    if needed_lanes <= len(free_lanes):
                        old_lanes = booked_lanes.objects.filter(booking_id=booking_id)
                        old_lanes.delete()
                        add_lanes_to_booking(request, form, needed_lanes, free_lanes, req_time)
                        form.instance.time_slot = req_time
                        booking = form.save(commit=False)
                        booking.save()
                        messages.success(request, 'The booking was successfully edited!')
                        return redirect('bookings-index')
                    else:
                        messages.error(request, 'There are not enough lanes available for this booking')

                else:
                    messages.error(request, 'The date you entered is in the past')
            else:
                messages.error(request, 'The amount of players must be at least 1')
    else:
        form = CreateBookingForm(instance=booking)
    return render(request, 'bookings/edit_booking.html', {'form': form,
                                                          'booking': booking
                                                          })


def add_lanes_to_booking(request, form, needed_lanes, free_lanes, req_time):
    for i in range(needed_lanes):
        booked_lane = booked_lanes()
        booked_lane.booking = form.instance
        booked_lane.lane_nr = free_lanes[i]
        booked_lane.time_slot = req_time
        booked_lane.date = request.POST['date']
        booked_lane.save()
