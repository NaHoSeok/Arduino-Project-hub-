void setup() {
  // put your setup code here, to run once:
  // DC motor 사용법은 LED on/off와 동일
  // DC motor: port 2개 필요
  // motor 초기화
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(2, HIGH);  // 5V 인가
  digitalWrite(3, LOW);   // 0V 인가
  delay(1000);            // 1000ms 동안 회전
  // 역방향 회전
  digitalWrite(2, LOW);   // 5V 인가
  digitalWrite(3, HIGH);  // 0V 인가
  delay(1000);            // 1000ms 동안 회전
}
