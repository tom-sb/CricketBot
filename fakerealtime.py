import serial
import time
import paho.mqtt.client as mqtt_pub
from random import uniform

mqttBroker = "34.72.145.97"
client = mqtt_pub.Client()
client.connect(host='34.72.145.97',port=1883,keepalive=45)
arduino_connect = serial.Serial('COM3',9600)

while True:
    data = arduino_connect.readline()
    topic = data.split()

    humedad = topic[0]
    temperatura = topic[1]
    humedad_suelo = topic[2]
    randNumber = uniform(20.0,21.0)
    client.publish("Humedad",humedad) #str(randNumber))
    time.sleep(1)
    client.publish("Temperatura",temperatura) #str(randNumber))
    time.sleep(1)
    client.publish("Humedad_suelo",humedad_suelo) #str(randNumber))
    time.sleep(1)
client.disconnect()
