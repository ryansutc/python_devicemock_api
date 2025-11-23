
from datetime import datetime
from time import time
from rest_framework import serializers

from devicemock.models.device import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    cur_val = serializers.SerializerMethodField()
    
    class Meta:
        model = Device
        fields = ["url", "name", "path", "value", "on", "value_update_interval", "device_type", "cur_val"]
    
    def get_cur_val(self, obj):
        """Calculate cur_val as value + current seconds"""
        return obj.value + datetime.now().second

