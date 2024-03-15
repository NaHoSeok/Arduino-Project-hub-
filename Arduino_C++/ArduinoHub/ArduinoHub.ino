#include "ArduinoHub.h"
#define SERIAL_RATE (9600)

/* [ArduinoHub 명령어]
0. 명령어 끝은 엔터(\n)로 끝남
1. 전압 읽기: get volt
2. 조도 스텝 읽기: get lightstep
3-1. 서보 모터 구동: set servo #pos (#pos: 각도를 숫자(#)로 입력)
3-2. DC 모터 구동: set dcmotor #pos (#pos: 각도를 숫자(#)로 입력)
4. 3색 LED 출력: set led color (color: 색깔 문자열)
5. 부저 출력: set buzzer note #delay (note: 음정 문자열, #delay: 음 지속 시간을 msec)
*/
ArduinoHub arduinoHub;

void setup() {
    // put your setup code here, to run once:
  arduinoHub.setup();
  Serial.begin(SERIAL_RATE);
}

void loop() {
  // put your main code here, to run repeatedly:
  arduinoHub.start();
}