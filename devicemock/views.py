from rest_framework import permissions, viewsets
from devicemock.models.device import Device
from devicemock.serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('id')
    serializer_class = DeviceSerializer