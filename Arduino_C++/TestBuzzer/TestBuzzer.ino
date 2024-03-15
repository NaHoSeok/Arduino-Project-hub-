void setup() {
  // put your setup code here, to run once:
  pinMode(8, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  tone(8, 523, 1000);
  delay(1100);
  tone(8, 587, 1000);
  delay(1100);
  tone(8, 659, 1000);
  delay(1100);
}