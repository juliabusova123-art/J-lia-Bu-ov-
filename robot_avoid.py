import time
import RPi.GPIO as GPIO

SERVO_GPIO = 5

SERVO_PWM_HZ = 50

US_TRIG_GPIO = 20
US_ECHO_GPIO = 21

MOTOR_L_PWM = 13
MOTOR_R_PWM = 12

SWITCH_GPIO = 19

PWM_HZ_MOTORS = 1000

def read_distance_cm(timeout_s=0.03) -> float:
	GPIO.output(US_TRIG_GPIO, GPIO.LOW)
	time.sleep(0.0002)
	GPIO.output(US_TRIG_GPIO, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(US_TRIG_GPIO, GPIO.LOW)

	t0 = time.time()


	while GPIO.input(US_ECHO_GPIO) == 0:
		if time.time() - t0 > timeout_s:
			return float("inf")
	pulse_start = time.time()


	while GPIO.input(US_ECHO_GPIO) == 1:
		if time.time() - pulse_start > timeout_s:
			return float("inf")
	pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	return pulse_duration * 17150.0


def servo_angle_to_duty(angle_deg: float) -> float:
	pulse_ms = 1.0 + (angle_deg / 180.0)
	return (pulse_ms / 20.0) * 100.0

def set_servo(pwm, angle_deg: float):
	duty = servo_angle_to_duty(max(0.0, min(180.0, angle_deg)))
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.25)


def motors_setup():
	GPIO.setup(MOTOR_L_PWM, GPIO.OUT)
	GPIO.setup(MOTOR_R_PWM, GPIO.OUT)

	lpwm = GPIO.PWM(MOTOR_L_PWM, PWM_HZ_MOTORS)
	rpwm = GPIO.PWM(MOTOR_R_PWM, PWM_HZ_MOTORS)
	lpwm.start(0)
	rpwm.start(0)

	return lpwm, rpwm

def motors_stop(lpwm, rpwm):
	lpwm.ChangeDutyCycle(0)
	rpwm.ChangeDutyCycle(0)

def motors_drive(lpwm, rpwm, speed_left=60, speed_right=60, forward=True):
	lpwm.ChangeDutyCycle(max(0, min(100, speed_left)))
	rpwm.ChangeDutyCycle(max(0, min(100, speed_right)))

def turn_in_place(lpwm, rpwm, speed=55, left=True, duration=0.35):
	if not left:
		motors_drive(lpwm, rpwm, speed_left=0, speed_right=speed, forward=True)
	else:
		motors_drive(lpwm, rpwm, speed_left=speed, speed_right=0, forward=True)
	time.sleep(duration)


def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	GPIO.setup(US_TRIG_GPIO, GPIO.OUT)
	GPIO.setup(US_ECHO_GPIO, GPIO.IN)

	GPIO.setup(SERVO_GPIO, GPIO.OUT)
	GPIO.setup(SWITCH_GPIO, GPIO.IN)

	servo_pwm = GPIO.PWM(SERVO_GPIO, SERVO_PWM_HZ)
	servo_pwm.start(0)

	lpwm, rpwm = motors_setup()

	try:
		set_servo(servo_pwm, 90)

		time.sleep(0.05)

		print("Caka na tlacidko")
		while GPIO.input(SWITCH_GPIO) == 0:
			time.sleep(0.1)

		print("Štartujem jazdu.")
		time.sleep(0.5)
		motors_drive(lpwm, rpwm, 65, 65, forward=True)

		STOP_DIST = 20.0 
		LOOP_DT = 0.05

		while True:
			if GPIO.input(SWITCH_GPIO) == 1:
				break
			dist = read_distance_cm()

			if dist < STOP_DIST:
				motors_stop(lpwm, rpwm)
				time.sleep(0.05)

				set_servo(servo_pwm, 150)
				d_left = read_distance_cm()
				time.sleep(0.05)

				set_servo(servo_pwm, 30)
				d_right = read_distance_cm()
				time.sleep(0.05)

				set_servo(servo_pwm, 90)

				if d_left > d_right:
					turn_in_place(lpwm, rpwm, speed=55, left=True, duration=0.40)
				else:
					turn_in_place(lpwm, rpwm, speed=55, left=False, duration=0.40)

				motors_drive(lpwm, rpwm, 65, 65, forward=True)

			time.sleep(LOOP_DT)

	except KeyboardInterrupt:
		print("\nKoniec (CTRL+C).")

	finally:
		motors_stop(lpwm, rpwm)
		servo_pwm.stop()
		lpwm.stop()
		rpwm.stop()
		GPIO.cleanup()

if __name__ == "__main__":
	main()
