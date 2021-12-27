import paho.mqtt.client as mqtt
from realtime.messaging import send_new_topic
import time
#from sensorData.utils import create_sensorData

def on_connect(client, user_data, flags, rc):
    #print('connect (%s)' % client._client_id)
    client.subscribe("#") #topic='TEMPERATURE', qos=2)

def on_message(client,user_data, message):
    #print(message.topic)
    data = { "topic": message.topic,
            "payload": message.payload.decode("utf-8"),
            "qos": message.qos}
    #print(type(message.payload))
    send_new_topic(data)

client = mqtt.Client("Smartphone")#client_id='robotica-subs', clean_session=False)

time.sleep(10)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host='34.72.145.97', port=1883)
#client.loop_forever()