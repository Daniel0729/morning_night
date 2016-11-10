from __future__ import unicode_literals
from sun import sunrisetime

from django.db import models

# Create your models here.
class wakeup(models.Model):
    #sunrisetime = models.DateTimeField(sunrisetime())
    wakeuptime_plan = models.DateTimeField()
    wakeuptime = models.DateTimeField()
    wakeupmood = models.BooleanField()
