#include "StringTok.h"

StringTok stInput;  // StringTok 클래스의 인스턴스로 stInput 선언

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Serial로부터 문장 읽기
  stInput.appendSerial();  // append(추가하기)
  // 사용자 입력: stInput은 문장을 저장
  // 사용자 미입력: stInput은 empty
  if (!stInput.isEmpty())   // stInput이 empty인지 확인 -> NOT 연산(!)
  {                         // 사용자 입력 있음: stInput is not(!) empty
    if (stInput.hasLine())  // stInput 안에 엔터(\n)가 있는가?
    {
      // 명령어 조건: 명령어 뒤에는 반드시 엔터(\n)이 들어감
      // StringTok을 String으로 바꾸어서 Serial에 출력
      Serial.println("input = [" + stInput.toString() + "]");
      // 토큰(token) 가져오기: 원래 문장을 건드리지 않음
      //StringTok stToken = stInput.getToken();
      // 문장에서 토큰을 잘라서 가져오기: 토큰만큼 원래 문장이 줄어듬
      StringTok stToken = stInput.cutToken();
      Serial.println("token = [" + stToken.toString() + "]");
      delay(2000);  // 2000ms 지연
    }
  }
}