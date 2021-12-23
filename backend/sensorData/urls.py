from django.urls import path, include
from sensorData.views import DataMqttAPIView, DataImageAPIView
from sensorData.views import CreateDataMqttAPIView, CreateDataImageAPIView

urlpatterns = [
    path('register_data', CreateDataMqttAPIView.as_view(), name='register data'),
    path('register_image', CreateDataImageAPIView.as_view(), name='register image'),
    path('detail_data/<slug:id>', DataMqttAPIView.as_view(), name=' topic detail'),
    path('detail_image/<slug:id>', DataImageAPIView.as_view(), name= 'image detail'),
]