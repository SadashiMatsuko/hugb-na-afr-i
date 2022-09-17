from django.db import models

# Create your models here.
class lanes(models.Model):
    lane_nr = models.IntegerField(primary_key=True)


class booking_time_slots(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self):
        return str(self.start_time)[:-3] + ' - ' + str(self.end_time)[:-3]


class bookings(models.Model):
    booker_phone = models.CharField(max_length=15, default="xxx-xxxx")
    date = models.DateTimeField(null=True)
    time_slot = models.ForeignKey(booking_time_slots, on_delete=models.CASCADE)
    player_amount = models.IntegerField(default=1)
    payed = models.BooleanField(default=False)


class booked_lanes(models.Model):
    booking = models.ForeignKey(bookings, on_delete=models.CASCADE)
    lane_nr = models.ForeignKey(lanes, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(booking_time_slots, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('booking', 'lane_nr', 'time_slot', 'date')

    def __str__(self):
        return str(self.lane_nr) + ' ' + str(self.time_slot) + ' ' + str(self.date)
