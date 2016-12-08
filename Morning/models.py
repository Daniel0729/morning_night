from __future__ import unicode_literals
from django.db import models

# Create your models here.
class MLight_State(models.Model):
    light = models.CharField(max_length=10)


class Music_State(models.Model):
    music = models.CharField(max_length=10)


# class Wakeup(models.Model):
#     wakeuptime = models.DateTimeField(auto_now=False, auto_now_add=True)
#     wakeuptime_plan = models.DateTimeField(auto_now=True, auto_now_add=False)
#     wakeupmood = models.CharField(max_length=100)
