from sensorData.models import DataMqtt

def create_sensorData(topic,payload,qos):
    data=DataMqtt.objects.create(topic=topic,payload=payload,qos=qos)
    data.save()
    return data