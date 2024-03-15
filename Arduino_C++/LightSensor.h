#pragma once
#include "Voltmeter.h"

#define DEF_LIGHT_PORT (A1)	// defalut�� ����

class LightSensor : public Voltmeter	// Voltmeter Ŭ������ public���� ��ӹ޾�(:) LightSensor Ŭ���� ����
{
public:
	LightSensor(void) { setPort(DEF_LIGHT_PORT); }	// fsetPort�� LightSensor�� ���ǵ��� ����;
													// �θ� Ŭ������ Voltmeter�� ����
	~LightSensor(){}

	int getLightStep(void) const { return getVoltStep(); }

private:
};
