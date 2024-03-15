#include "MyServo.h"  // "...": 현재 스케치 폴더에서 헤더 파일 검색하여 include

MyServo myServo;

void setup() {
  // put your setup code here, to run once:
  myServo.setup();
  myServo.move(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  myServo.move(90);
  myServo.move(180);
  myServo.move(90);
  myServo.move(0);
}