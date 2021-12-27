from rest_framework import serializers
from sensorData.models import DataMqtt, DataImage

import base64
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def from_native(self, data):
        if isinstance(data, basestring) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super(Base64ImageField, self).from_native(data)

class DataMQTTSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMqtt
        fields = '__all__'

class DataImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = DataImage
        fields = ('image','accuracy','disease_name',)
        extra_kwargs = {
            'accuracy': {'read_only': True},
            'disease_name' : {'read_only': True}
        }