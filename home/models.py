from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Wakeup(models.Model):
     wakeuptime = models.DateTimeField(auto_now=False,auto_now_add=True)
     wakeuptime_plan = models.DateTimeField(auto_now=True,auto_now_add=False)
     wakeupmood = models.CharField(max_length=100)
     # timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

     def get_absolute_url(self):
          return reverse("home")
