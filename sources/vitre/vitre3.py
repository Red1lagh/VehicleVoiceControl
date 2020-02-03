import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

pwm=GPIO.PWM(17,100)
pwm.start(5)

angle1 = -15
duty1 = float(angle1)/10 + ajoutAngle

pwm.ChangeDutyCycle(duty1)
time.sleep(0.8)
GPIO.cleanup()
