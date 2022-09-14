from django.db import models

# Create your models here.
class lanes(models.Model):
    lane_nr = models.IntegerField(primary_key=True)


class bookings(models.Model):
    lane_nr = models.ForeignKey(lanes, on_delete=models.CASCADE)
    booker_phone = models.CharField(max_length=13, default="No phone")
    start_time = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    payed = models.BooleanField(default=False)