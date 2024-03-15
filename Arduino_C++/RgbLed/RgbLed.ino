#include "RgbLed.h"

RgbLed rgbLed;

void setup() {
  // put your setup code here, to run once:
  rgbLed.setup();
}

void loop() {
  // put your main code here, to run repeatedly:
  rgbLed.turnRgb(CT_RED);  // red
  delay(1000);
  rgbLed.turnRgb(CT_GREEN);  // green
  delay(1000);
  rgbLed.turnRgb(CT_BLUE);  // blue
  delay(1000);
  rgbLed.turnRgb(CT_BLACK);  // black
  delay(1000);
  rgbLed.turnRgb(CT_WHITE);  // white
  delay(1000);
}