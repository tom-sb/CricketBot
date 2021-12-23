# /bin/env
import ssl
import sys

import paho.mqtt.client as mqtt
import time

"""def on_message(client,user_data,message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)

client.loop_end()"""

def on_connect(client, user_data, flags, rc):
    print('connect (%s)' % client._client_id)
    client.subscribe(topic='TEMPERATURE', qos=2)

def on_message(client,user_data, message):
    print('---------------------------')
    print('topic: %s' % message.topic)
    print('payload: %s' % message.payload)
    print('qos: %s' % message.qos)

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(client_id='robotica-subs', clean_session=False)

client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttBroker)#host='127.0.0.1', port=1883)
client.loop_forever()
