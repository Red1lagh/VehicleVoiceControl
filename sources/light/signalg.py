
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)

for i in range(5):
 
   GPIO.output(5,1)
   time.sleep(0.5)
   GPIO.output(5,0)
   time.sleep(0.5)

os.system('omxplayer -o local /home/PFA_ADAS/SYNTHESE/Eclairage_signal/signal_gauche/rep_desac_sigg.wav')








