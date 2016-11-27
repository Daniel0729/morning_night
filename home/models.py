from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Wakeup(models.Model):
     wakeuptime = models.DateTimeField()
     wakeuptime_plan = models.DateTimeField()
     wakeupmood = models.CharField(max_length=100)


