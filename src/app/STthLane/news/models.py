from django.db import models
from datetime import datetime


# Create your models here.
class articles(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)
    # author foreign key to employee/user on_delete = models.CASCADE
    def __str__(self):
        return self.title
