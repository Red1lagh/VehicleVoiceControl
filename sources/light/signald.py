
import time
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)

for i in range(5):
 
   GPIO.output(6,1)
   time.sleep(0.5)
   GPIO.output(6,0)
   time.sleep(0.5)


os.system('omxplayer -o local /home/PFA_ADAS/SYNTHESE/Eclairage_signal/signal_droit/rep_desac_sigd.wav')
#  os.system('omxplayer -o local /home/PFA_ADAS/SYNTHESE/Eclairage_signal/signal_gauche/rep_desac_sigg.wav')

