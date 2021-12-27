import paho.mqtt.client as mqtt
from realtime.messaging import send_new_topic
import time
#from sensorData.utils import create_sensorData

def on_connect(client, user_data, flags, rc):
    #print('connect (%s)' % client._client_id)
    client.subscribe("#") #topic='TEMPERATURE', qos=2)

def on_message(client,user_data, message):
    #print(message.topic)
    data1 = { "topic": message.topic,
            "payload": message.payload.decode("utf-8").replace('\r','').replace('\n',''),
            "qos": message.qos}
    Topic = ['Temp','Hume','Soil']
    data = message.payload.decode("utf-8").replace("\r",'').replace("\n",'').split('\t')
    print(data, message.payload.decode("utf-8"))
    if len(data)>1:
        for i in range(len(data)):
            topic = { "topic": Topic[i],
                        "payload": data[i],
                        "qos": message.qos}
            print(topic)
            send_new_topic(topic)
    else:
        send_new_topic(data1)

client = mqtt.Client("Smartphone")#client_id='robotica-subs', clean_session=False)

time.sleep(10)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host='34.72.145.97', port=1883)
#client.loop_forever()