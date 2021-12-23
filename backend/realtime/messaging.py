from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.db import  database_sync_to_async

from realtime.events import NewDataEvent, NewDataImage

#@database_sync_to_async
def dataCreate(topic,payload,qos):
    from sensorData.models import DataMqtt
    data = DataMqtt.objects.create(topic=topic,
                                payload=payload,
                                qos=qos)
    data.save()
    return data

channel_layer = get_channel_layer()

def send_new_topic(topic):
    topic = dataCreate(topic=topic['topic'],
                            payload=topic['payload'],
                            qos=topic['qos'])
    #print(topic)
    _send_realtime_event_to_user(
        realtime_event=NewDataEvent(
            id=topic.id,
            topic=topic.topic,
            payload=topic.payload,
            timestamp=topic.timestamp,
            qos=topic.qos,
        )
    )

def send_new_image(dataImg):
    _send_realtime_event_to_user(
        realtime_event=NewDataImage(
            id = dataImg.id,
            image = dataImg.image,
        )
    )

"""def _send_realtime_img(realtime_event):
    async_to_sync(channel_layer.send)(
        "realtime-img",
        {
            'type': 'send_event',
            'realtime_img': realtime_event.properties_dict,
        }
    )"""

def _send_realtime_event_to_user(realtime_event):
    async_to_sync(channel_layer.send)(
        "realtime-mqtt",
        {
            'type': 'send_event',
            'realtime_mqtt': realtime_event.properties_dict,
        }
    )