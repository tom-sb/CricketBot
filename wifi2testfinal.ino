#include <ESP8266WiFi.h>
#include <PubSubClient.h>
const char* ssid = "chickenbone";
const char* password = "server4cs";
const char* mqtt_server = "34.72.145.97";
WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;
void setup_wifi() {
  delay(10);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  randomSeed(micros());
}
void callback(char* topic, byte* payload, unsigned int length) {
  String topicStr = topic;
  if (payload[0] == '1') {
    Serial.print("1");
    respond();
  } else {
    Serial.print("0");
    respond();
  }
}
char* toCharArray(String str) {
  return &str[0];
}
void respond(){
  delay(5);
  if(Serial.available()){
    String sendmsg = Serial.readString();
    if(sendmsg[0] == 't'){
      client.publish("Temp", toCharArray(sendmsg));
    }else if(sendmsg[0] == 'h'){
      client.publish("Hume", toCharArray(sendmsg));
    }else if(sendmsg[0] == 's'){
      client.publish("Soil", toCharArray(sendmsg));
    }
  }
}
void reconnect() {
  while (!client.connected()) {
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      client.subscribe("inTopic");
    } else {
      delay(5000);
    }
  }
}
void setup() {
  Serial.begin(9600);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}


void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  delay(5000);
  Serial.println(Serial.available());
  Serial.println("1");
  String sendmsg = Serial.readString();
  client.publish("SensorData", toCharArray(sendmsg));
}
