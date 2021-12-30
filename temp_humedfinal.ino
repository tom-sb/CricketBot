#include <dht.h>

dht DHT;
#define DHT11_PIN 8
#define NOTE_B0  31
#define NOTE_C1  33
#define NOTE_B1  62

const int sensorPin = A0;
const int buzzer = 10;
void setup() {
  Serial.begin(9600);
}
int funcSenSoil(){
  int soilhum = analogRead(sensorPin);
  int soilp = map(soilhum,300,1023,100,0);
  return soilp;
}
void funcActTH(){
  DHT.read11(DHT11_PIN);
}
int funcSenTemp(){
  return DHT.temperature;
}
int funcSenHume(){
  return DHT.humidity;
}

void funcCri(){
  const float songSpeed = 1.0;
  int notes[] = {
    NOTE_C1, NOTE_B0, 0, 0, 0,
    NOTE_B1, NOTE_B0, 0, 0, 0,
    NOTE_B1, NOTE_B0, 0, 0, 0,
    NOTE_C1, NOTE_B0, 0, 0, 0,
    NOTE_C1, NOTE_B0, 0, 0, 0,
    NOTE_B1, NOTE_B0};
  int durations[] = {
    50, 50, 250, 125, 175,
    50, 70, 50, 125, 75,
    50, 70, 250, 125, 375,
    50, 50, 250, 125, 175,
    50, 70, 250, 25, 25,
    50, 70};
  const int totalNotes = sizeof(notes) / sizeof(int);
  for (int i = 0; i < totalNotes; i++){
    const int currentNote = notes[i];
    float wait = durations[i] / songSpeed;
    if (currentNote != 0){
      tone(buzzer, notes[i], wait); // tone(pin, frequency, duration)
    }else{
      noTone(buzzer);
    }
    delay(wait);
  }
}


void loop() {
    char getmsg = Serial.read();
    funcActTH();
    if(getmsg == '1'){
      funcCri();
    }
    Serial.println(funcSenTemp());
    Serial.print("\t");
    Serial.println(funcSenHume());
    Serial.print("\t");
    Serial.print(funcSenSoil());
    Serial.println("\n");
    delay(5000);
    if(funcSenSoil() < 20){
      funcCri();
    }
}
