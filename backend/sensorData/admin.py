from django.contrib import admin
from sensorData.models import DataMqtt, DataImage

admin.site.register(DataMqtt)
admin.site.register(DataImage)