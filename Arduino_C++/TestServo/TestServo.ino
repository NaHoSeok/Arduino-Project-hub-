#include <Servo.h>  // <>: Arduino가 제공하는 헤더 파일 폴더 검색해서 include

// Servo-motor 결선도
// 빨간색(중앙의 도선): +5V 연결
// 갈색: 0V(GND) 연결
// 주황색: digital port(2~13) 연결

Servo servo;  // Servo 클래스의 실행 결과물로 인스턴스 servo를 선언

void setup() {
  // put your setup code here, to run once:
  // 서보 모터를 제어할 digital port 연결
  servo.attach(4);  // D4에 서보 모터의 제어선 연결
  servo.write(0);   // 서보 모터 위치를 0으로 이동
  delay(1000);      // 1000ms 동안 기다림: 서보 모터가 이동할 시간을 줌
}

void loop() {
  // put your main code here, to run repeatedly:
  // 서보 모터 이동 범위: 0도 ~ 180도만 이동 가능
  // DC 모터: 모든 각도로 이동 가능; 여러 번 회전도 가능
  servo.write(180);  // 180도 위치로 이동
  delay(1000);       // 1000ms 기다림
  servo.write(0);    // 180도 위치로 이동
  delay(1000);       // 1000ms 기다림
}