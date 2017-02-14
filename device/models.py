from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class DeviceType(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

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
    
    class Meta:
        ordering = ('name',)
    def __unicode__(self):
        return self.name