from rest_framework import serializers
from sensorData.models import DataMqtt, DataImage

class DataMQTTSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMqtt
        fields = '__all__'

class DataImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataImage
        fields = ('image',)