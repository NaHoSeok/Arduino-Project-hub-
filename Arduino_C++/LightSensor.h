#pragma once
#include "Voltmeter.h"

#define DEF_LIGHT_PORT (A1)	// defalut값 정의

class LightSensor : public Voltmeter	// Voltmeter 클래스를 public으로 상속받아(:) LightSensor 클래스 구현
{
public:
	LightSensor(void) { setPort(DEF_LIGHT_PORT); }	// fsetPort는 LightSensor에 정의되지 않음;
													// 부모 클래스인 Voltmeter에 정의
	~LightSensor(){}

	int getLightStep(void) const { return getVoltStep(); }

private:
};
