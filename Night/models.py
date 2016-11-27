from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Light_State(models.Model):
    light = models.CharField(max_length=10)


class Curtain_State(models.Model):
    curtain = models.CharField(max_length=10)
