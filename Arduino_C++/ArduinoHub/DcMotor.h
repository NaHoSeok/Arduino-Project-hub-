#pragma once

#define DEF_DC_MOTOR_PORT1	(2)
#define DEF_DC_MOTOR_PORT2	(3)
#define DC_MOTOR_SPEED	(360./950.) // 단위: 각도/시간(msec)

class DcMotor
{
public:
	DcMotor(void) { setPort(DEF_DC_MOTOR_PORT1, DEF_DC_MOTOR_PORT2); }
	~DcMotor() {}

	void setPort(int nPort1, int nPort2)
	{
		m_nPort1 = nPort1;
		m_nPort2 = nPort2;
	}
	void setup(void)
	{
		initMotor();
		stopMotor();
	}
	void move(int nPos) // nPos: 어떤 각도든지 이동; (+)이면 정방향, (-)이면 역방향
	{
		int nDelay = int(abs(nPos) / DC_MOTOR_SPEED + 0.5);
		if (nPos >= 0) setFwdMove();
		else setBackMove();
		delay(nDelay);
		stopMotor();
	}

private:
	int m_nPort1, m_nPort2;

	void initMotor(void)
	{
		pinMode(m_nPort1, OUTPUT);
		pinMode(m_nPort2, OUTPUT);
	}
	void stopMotor(void)
	{
		digitalWrite(m_nPort1, LOW);
		digitalWrite(m_nPort2, LOW);
	}
	void setFwdMove(void) // forward move (정방향 이동)
	{
		digitalWrite(m_nPort1, HIGH);
		digitalWrite(m_nPort2, LOW);
	}
	void setBackMove(void) // backward move (역방향 이동)
	{
		digitalWrite(m_nPort1, LOW);
		digitalWrite(m_nPort2, HIGH);
	}
};