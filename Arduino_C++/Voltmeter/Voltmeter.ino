#include "Voltmeter.h"  // 현재 폴더에서 헤더 파일 검색
//#include <Voltmeter.h>  // Arduino IDE가 사용하는 include 폴더 검색
#include "LightSensor.h"

Voltmeter voltmeter;  // Voltmeter란 클래스를 voltmeter란 인스턴스로 생성
LightSensor lightSensor;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lightSensor.setPort(A2);
}

void loop() {
  // put your main code here, to run repeatedly:
  int nVolt = voltmeter.getVoltStep();
  Serial.println("step = " + String(nVolt));
  double volt = voltmeter.getVolt();
  Serial.println("volt = " + String(volt));
  int nLight = lightSensor.getLightStep();
  Serial.println("\nlight = " + String(nLight));
  int nLightState = lightSensor.getLightState();
  Serial.println("light state = " + String(nLightState));
  Serial.println("light state = " + lightSensor.lightStateToStr(nLightState));
  delay(1000);
}