#from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
#from channels import route
from channels.auth import AuthMiddlewareStack
#from sensorData.consumers import MqttConsumer #, on_mqtt_message
from realtime.consumers import EventSenderConsumer

application = ProtocolTypeRouter({
    #'http': get_asgi_application(),
    'channel': ChannelNameRouter({
        "realtime-mqtt": EventSenderConsumer.as_asgi(),
    }),
})