from .models import Device,DeviceType, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import pagination, serializers
from django.contrib.auth.models import User, Group
from rest_framework_gis import serializers as gis_serializers

class DeviceTypeSerializer(serializers.HyperlinkedModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    class Meta:
        model = DeviceType
        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'name', 'desc')


class DeviceSerializer(gis_serializers.GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    class Meta:
        model = Device
        geo_field = "location"
        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'name', 'desc','message','location')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')