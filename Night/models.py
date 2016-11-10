from __future__ import unicode_literals

from django.db import models
from sun import sunsettime
# Create your models here.
class night(models.Model):
    sunrisetime = models.DateTimeField(sunsettime())
