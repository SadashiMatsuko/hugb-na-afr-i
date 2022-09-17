from django.db import models

# Create your models here.
class lanes(models.Model):
    lane_nr = models.IntegerField(primary_key=True)


class booking_time_slots(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()


class bookings(models.Model):
    lane_nr = models.ForeignKey(lanes, on_delete=models.CASCADE)
    booker_phone = models.CharField(max_length=13, default="No phone")
    date = models.DateTimeField(null=True)
    time_slot = models.CharField(max_length=13, default="No time slot")
    payed = models.BooleanField(default=False)


