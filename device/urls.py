from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^devices/$', views.device_list),
    url(r'^devices/(?P<pk>[0-9]+)/$', views.device_detail),
    url(r'^devicetypes/$', views.deviceType_list),
    url(r'^devicetypes/(?P<pk>[0-9]+)/$', views.deviceType_detail),
]