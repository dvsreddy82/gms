from rest_framework import serializers
from .models import Device,DeviceType, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import pagination, serializers
from rest_framework_gis import serializers as gis_serializers

class DeviceTypeSerializer(serializers.ModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    #details = serializers.HyperlinkedIdentityField(view_name='api_geojson_location_details')
    class Meta:
        model = DeviceType
        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'name', 'desc')


class DeviceSerializer(gis_serializers.GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    #details = serializers.HyperlinkedIdentityField(view_name='api_geojson_location_details')
    class Meta:
        model = Device
        geo_field = "location"


        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'name', 'desc','message','location')