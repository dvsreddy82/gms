from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class DeviceType(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Device(models.Model):
    """
    A model which holds information about a particular location
    """
    type = models.ForeignKey(DeviceType)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    location = models.PointField()

    def __unicode__(self):
        return self.name