#include <DHT.h>
#include <DHT_U.h>


// Incluimos librería
#include <DHT.h>
 
int Sensor=8;
int temp, humedad;
const byte SensorCO=0;  //pin analogico A0
float CO;
const float ADCV=5.0/1024.0;

DHT dht(Sensor, DHT11);

void setup(){
  Serial.begin(9600);
  dht.begin();
}
void loop(){
  humedad = dht.readHumidity();
  temp= dht.readTemperature();
  CO= analogRead(SensorCO)*ADCV;
  

  //Serial.print(" Temperatura: ");
  Serial.println( temp);

  //Serial.print(" Humedad: ");
  Serial.println( humedad);
 
  //Serial.print(" CO2: ");
  Serial.println( CO);
  
  delay(3000);
}
