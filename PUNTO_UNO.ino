#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define LED_VERDE 10
#define LED_ROJO 9

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_ROJO, OUTPUT);
  
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(LED_ROJO, LOW);
  
  Serial.println("Sistema listo");
}

void loop() {
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();
    
    if (comando == "ON_VERDE") {
      digitalWrite(LED_VERDE, HIGH);
      Serial.println("LED VERDE encendido");
    }
    else if (comando == "OFF_VERDE") {
      digitalWrite(LED_VERDE, LOW);
      Serial.println("LED VERDE apagado");
    }
    else if (comando == "ON_ROJO") {
      digitalWrite(LED_ROJO, HIGH);
      Serial.println("LED ROJO encendido");
    }
    else if (comando == "OFF_ROJO") {
      digitalWrite(LED_ROJO, LOW);
      Serial.println("LED ROJO apagado");
    }
    else if (comando == "TEMP") {
      float temp = dht.readTemperature();
      if (!isnan(temp)) {
        Serial.println(temp);
      } else {
        Serial.println("ERROR");
      }
    }
  }
  
  delay(100);
}