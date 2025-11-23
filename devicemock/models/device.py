import uuid
from django.db import models

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    value = models.IntegerField(null=False, blank=False, default=0)
    on = models.BooleanField(default=True)
    value_update_interval = models.IntegerField(null=False, blank=False, default=5)  # in seconds
    device_type = models.CharField(max_length=50, default="generic")

    class Meta:
        app_label = 'devicemock'

    def __str__(self):
        return f"{self.name} ({self.device_type})"