void setup() {
  // put your setup code here, to run once: 
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  // 3.3V -> A0: 선 연결
  int nVolt = analogRead(A0);   // A0 포트에서 아날로그 전압값 읽음 -> 0~1023 숫자로 바꿈
  // 0V -> nVolt = 0; 5V -> nVolt = 1023 (2^10 = 1024)
  double volt = 5./1023. * nVolt; // step -> 전압값
  Serial.println("volt = " + String(volt)); // String(volt) : double -> String
  delay(1000);  // 1000ms 지연 
}
