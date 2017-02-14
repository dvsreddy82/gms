from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Device,DeviceType
from .serializers import DeviceSerializer,DeviceTypeSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def device_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def deviceType_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        deviceTypes = DeviceType.objects.all()
        serializer = DeviceTypeSerializer(deviceTypes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeviceTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def deviceType_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        deviceType = DeviceType.objects.get(pk=pk)
    except DeviceType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DeviceTypeSerializer(deviceType)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DeviceTypeSerializer(deviceType, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        deviceType.delete()
        return HttpResponse(status=204)


@csrf_exempt
def device_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        device = Device.objects.get(pk=pk)
    except DeviceType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DeviceSerializer(device, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        device.delete()
        return HttpResponse(status=204)