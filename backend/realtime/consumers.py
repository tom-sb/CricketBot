import uuid
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from modules.inference import predict_class
from sensorData.models import DataImage
#from .websocket.utils import check_if_websocket_is_active
#from .websocket.messaging import send_event_via_websocket_group_consumer
pred = predict_class(home_path='./media')

@database_sync_to_async
def get_pred_data_image(pk,url):
    data = DataImage.objects.get(pk=pk)
    data.disease_name = pred.predict(url)
    data.save()

class EventSenderConsumer(AsyncConsumer):

    async def send_event(self, message):
        data = message['realtime_mqtt']
        """type_data = message['realtime_event_dict']['type']
        print(user, message)
        if await check_if_websocket_is_active(user):
            print("Realtime: event_sender_consumer_send_event - websocket branch")
            await send_event_via_websocket_group_consumer(
                channel_layer=self.channel_layer,
                user=user,
                realtime_event_dict=message['realtime_mqtt']
            )"""
        print(data)
        if data['type'] == 'data-image':
            v_url = data['image'].split('/')
            url = v_url[1] + '/' + v_url[2]
            await get_pred_data_image(data['id'],url)

