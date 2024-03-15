#include "Buzzer.h"

Buzzer buzzer;

void setup() {
  // put your setup code here, to run once:
  buzzer.setup();
}

void loop() {
  // put your main code here, to run repeatedly:
  buzzer.play(NT_DO, 1000);
  buzzer.play(NT_MI, 1000);
  buzzer.play(NT_SOL, 1000);
}