import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

pwm=GPIO.PWM(18,100)
pwm.start(5)

angle1 = 0
duty1 = float(angle1)/10 + ajoutAngle
angle2=160
duty2= float(angle2)/10 + ajoutAngle

i = 0
while i < 3:
        pwm.ChangeDutyCycle(duty1)
        time.sleep(1.4)
        pwm.ChangeDutyCycle(duty2)
        time.sleep(3.5)
    
        i = i+1
GPIO.cleanup()
