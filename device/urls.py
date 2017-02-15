from django.conf.urls import url,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'devicetypes', views.DeviceTypeViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]