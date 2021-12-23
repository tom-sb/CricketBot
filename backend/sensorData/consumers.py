import datetime
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer, AsyncConsumer
#from channels import Group


class MqttConsumer(SyncConsumer):

    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        print("topic: {0}, payload: {1}".format(topic, payload))

    def mqtt_pub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        print("topic: {0}, payload: {1}".format(topic, payload))

"""def on_mqtt_message(message):
    msg = "{}: {}".format(message.content["topic"],
                          message.content["payload"].decode("utf-8"))
    Group("mqtt").send({
        "text": msg
    })"""