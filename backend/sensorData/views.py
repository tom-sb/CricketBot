from rest_framework import generics, status
from rest_framework.response import Response
from sensorData.models import DataMqtt, DataImage
from sensorData.serializers import DataMQTTSerializer, DataImageSerializer
from realtime.messaging import send_new_image
class CreateDataMqttAPIView(generics.ListCreateAPIView):
    serializer_class = DataMQTTSerializer
    queryset = DataMqtt.objects.all()

class DataMqttAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DataMQTTSerializer
    queryset = DataMqtt.objects.all()
    lookup_field = 'id'

class CreateDataImageAPIView(generics.ListCreateAPIView):
    serializer_class = DataImageSerializer
    queryset = DataImage.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        send_new_image(data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class DataImageAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DataImageSerializer
    queryset = DataImage.objects.all()
    lookup_field = 'id'

