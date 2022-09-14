from django.db import models


# Create your models here.
class lanes(models.Model):
    lane_nr = models.IntegerField(primary_key=True)