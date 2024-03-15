#pragma once

#include "StringTok.h"
#include "Voltmeter.h"
#include "LightSensor.h"
#include "MyServo.h"
#include "RgbLed.h"
#include "Buzzer.h"

class ArduinoHub
{
public:
	ArduinoHub(void) {}
	~ArduinoHub() {}

	void setup(void) // actuator �ʱ�ȭ
	{
		m_myServo.setup();
		m_rgbLed.setup();
		m_buzzer.setup();
	}

	void start(void)
	{
		while (1) // 무한 반복
		{
			m_stInput.appendSerial();
			if (m_stInput.hasLine()) // 명령어 정상 입력
				exeCmd(); // 명령어 실행
		}
	}

	void exeCmd(void)
	{
		//Serial.println("input = [" + m_stInput.toString() + "]");
		String sToken = m_stInput.cutToken().toString();
		//Serial.println("token #1 = [" + sToken + "]");
		if (sToken == "get") exeGet();
		else if (sToken == "set") exeSet();
		else m_stInput.cutLine(); // 잘못된 명령 -> 현재 줄을 삭제
	}

  void exeSet(void) // get 명령어 실행
	{
		String sToken = m_stInput.cutToken().toString();
		if (sToken == "servo") exeServo();
		else if (sToken == "led") exeLed();
		else if (sToken == "buzzer") exeBuzzer();
		else m_stInput.cutLine();
	}

	void exeGet(void) // get 명령어 실행
	{
		// 1. 전압 읽기: get(#1) volt(#2)
		String sToken = m_stInput.cutToken().toString();
		//Serial.println("token #2 = [" + sToken + "]");
		if (sToken == "volt") exeVolt();
		else if (sToken == "light") exeLight();
		else if (sToken == "lightstep") exeLightStep();
		else m_stInput.cutLine();
	}

	void exeVolt(void)
	{
		double volt = m_voltmeter.getVolt();
		Serial.println(String(volt, 10)); // Serial에 출력
	}

	void exeLight(void)
	{
		int nLightState = m_lightSensor.getLightState();
		String sLightState = m_lightSensor.lightStateToStr(nLightState);
		Serial.println(sLightState);
	}

	void exeLightStep(void)
	{
		int nLightState = m_lightSensor.getLightStep();
		Serial.println(nLightState);
	}

	void exeServo(void)
	{
		String sToken = m_stInput.cutToken().toString();
		int nToken = sToken.toInt();
		if (nToken >= 0 && nToken <= 180)
		{
      Serial.println(sToken);
			m_myServo.move(nToken);
		}
		else
		{
			m_stInput.cutLine();
		}

	}

	void exeLed(void)
	{
		String sToken = m_stInput.cutToken().toString();
    Serial.println(sToken);
		if (sToken == "red")
		{
			m_rgbLed.turnRed(true);
			delay(2000);
			m_rgbLed.turnRed(false);
		}
		else if (sToken == "green")
		{
			m_rgbLed.turnGreen(true);
			delay(2000);
			m_rgbLed.turnGreen(false);
		}
		else if (sToken == "blue")
		{
			m_rgbLed.turnBlue(true);
			delay(2000);
			m_rgbLed.turnBlue(false);
		}
		else if (sToken == "pink")
		{
			m_rgbLed.turnRgb(CT_PINK);
			delay(2000);
			m_rgbLed.turnRgb(CT_BLACK);
		}
		else if (sToken == "yellow")
		{
			m_rgbLed.turnRgb(CT_YELLOW);
			delay(2000);
			m_rgbLed.turnRgb(CT_BLACK);
		}
		else if (sToken == "cyan")
		{
			m_rgbLed.turnRgb(CT_CYAN);
			delay(2000);
			m_rgbLed.turnRgb(CT_BLACK);
		}
		else if (sToken == "white")
		{
			m_rgbLed.turnRgb(CT_WHITE);
			delay(2000);
			m_rgbLed.turnRgb(CT_BLACK);
		}
		else { m_stInput.cutLine(); };	
	}

	void exeBuzzer(void)
	{
		String sToken = m_stInput.cutToken().toString();
		String sToken1 = m_stInput.cutToken().toString();
		if (sToken == "do") { m_buzzer.play(523, sToken1.toInt()); }
		else if (sToken == "re") { m_buzzer.play(587, sToken1.toInt()); }
		else if (sToken == "mi") { m_buzzer.play(659, sToken1.toInt()); }
		else if (sToken == "fa") { m_buzzer.play(698, sToken1.toInt()); }
		else if (sToken == "sol") { m_buzzer.play(784, sToken1.toInt()); }
		else if (sToken == "la") { m_buzzer.play(880, sToken1.toInt()); }
		else if (sToken == "si") { m_buzzer.play(988, sToken1.toInt()); }
	}

private:
	StringTok m_stInput;
	Voltmeter m_voltmeter;
	LightSensor m_lightSensor;
	MyServo m_myServo;
	RgbLed m_rgbLed;
	Buzzer m_buzzer;
};