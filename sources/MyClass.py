# -*- coding: utf-8 -*-

#!/usr/bin/env python3


import speech_recognition as sr
from time import ctime
import time
import os
from playsound import playsound
import arabic_reshaper
from bidi.algorithm import get_display
import RPi.GPIO as GPIO


class Audio:
    data = ""

    def recordAudio(self):
        # enregistrement Audio
        r = sr.Recognizer()
        r.energy_threshold = 16000
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            self.data = (r.recognize_google(audio, language="ar-MA"))
            self.data = (arabic_reshaper.reshape(data))
            self.data = get_display(data)
            print(self.data)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        return self.data


class Eclairage:

    def replique(path):
        print(path)
        os.system('omxplayer -o local '+path)

    c11 = get_display(arabic_reshaper.reshape("شعل الفار"))
    c12 = get_display(arabic_reshaper.reshape("شحال الفار"))
    c13 = get_display(arabic_reshaper.reshape("هل الفار"))
    c14 = get_display(arabic_reshaper.reshape("جعل الفار"))

    def activer_phare(self):
        self.replique("SYNTHESE/Eclairage_phare/rep_activ_phare.wav")
        GPIO.output(11, 1)

    c21 = get_display(arabic_reshaper.reshape("حبس الفار"))
    c22 = get_display(arabic_reshaper.reshape("في الفار"))
    c23 = get_display(arabic_reshaper.reshape("طفي الفار"))
    c24 = get_display(arabic_reshaper.reshape("حبس الغار"))

    def desactiver_phare(self):
        self.replique("SYNTHESE/Eclairage_phare/rep_desac_phare.wav")
        GPIO.output(11, 0)

    c31 = get_display(arabic_reshaper.reshape("شعل الكود"))
    c32 = get_display(arabic_reshaper.reshape("شحال الكود"))
    c33 = get_display(arabic_reshaper.reshape("هل الكود"))
    c34 = get_display(arabic_reshaper.reshape("جعل الكود"))

    def activer_code(self):
        self.replique("SYNTHESE/Eclairage_code/rep_activ_code.wav")
        GPIO.output(9, 1)

    c41 = get_display(arabic_reshaper.reshape("حبس الكود"))
    c42 = get_display(arabic_reshaper.reshape("في الكود"))

    def desactiver_code(self):
        self.replique("SYNTHESE/Eclairage_code/rep_desac_code.wav")
        GPIO.output(9, 0)

    c4 = get_display(arabic_reshaper.reshape("سينيال دليمن"))

    def signal_droit(self):
        self.replique("SYNTHESE/Eclairage_signal/signal_droit/rep_activ_sigd.wav")
        os.system("python /home/PFA_ADAS/light/signald.py")

    c5 = get_display(arabic_reshaper.reshape("سينيال دليسر"))
    def signal_gauche(self):
	self.replique("SYNTHESE/Eclairage_signal/signal_droit/rep_activ_sigg.wav")
	os.system("python /home/PFA_ADAS/light/signalg.py")

class Essuies_glaces:

	def replique(path):
    		print(path)
    		os.system('omxplayer -o local '+path)

	g1 = get_display(arabic_reshaper.reshape("شغل الماسحات"))

	def activer_essuies_glaces(self):
		self.replique("SYNTHESE/Gestion_essuie_glace/Activer_essuie_glace.wav")
	        os.system("python /home/PFA_ADAS/essuies_glaces/servo.py")
	g2 = get_display(arabic_reshaper.reshape("حول الى السرعة الأولى"))

	def essuie_glaces_vitesse1(self):
		self.replique("SYNTHESE/Gestion_essuie_glace/Switch_to_speed1.wav")
                os.system("python /home/PFA_ADAS/essuies_glaces/servo1.py")

	g3 = get_display(arabic_reshaper.reshape("حول الى السرعة الثانية"))

	def essuie_glaces_vitesse2(self):
                self.replique("SYNTHESE/Gestion_essuie_glace/Switch_to_speed2.wav")
                os.system("python /home/PFA_ADAS/essuies_glaces/servo2.py")

	g4 = get_display(arabic_reshaper.reshape("حول الى السرعة القصوى"))

	def essuie_glaces_top_vitesse(self):
                replique("SYNTHESE/Gestion_essuie_glace/Switch_to_top_speed.wav")
                os.system("python /home/PFA_ADAS/essuies_glaces/servo3.py")

	g5 = get_display(arabic_reshaper.reshape("حبس الماسحات"))

	def desactiver_essuies_glaces(self):
                self.replique(
                    "SYNTHESE/Gestion_essuie_glace/desactiver_essuie_glace.wav")
                os.system("python /home/PFA_ADAS/essuies_glaces/servo.py")


class Vitre:

	def replique(path):
    		print(path)
   		os.system('omxplayer -o local '+path)


class VitreGauche(Vitre):

	v1 = get_display(arabic_reshaper.reshape("فتح النافذَة د ليسر"))


²²²²def ouvrir():
		Vitre.replique("SYNTHESE/Controler_les_vitres/Open_left_win.wav")
                os.system("python /home/PFA_ADAS/vitre/vitre.py")

	v2=get_display(arabic_reshaper.reshape("النافذَة د ليسر على النيفو الاول"))
	def vitre_niv1():
		Vitre.replique("SYNTHESE/Controler_les_vitres/Level1_left_win.wav")
                os.system("python /home/PFA_ADAS/vitre/vitre1.py")

	v3=get_display(arabic_reshaper.reshape("النافذَة د ليسر على النيفو الثاني"))
	def vitre_niv2():
		Vitre.replique("SYNTHESE/Controler_les_vitres/Level2_left_win.wav")
                os.system("python /home/PFA_ADAS/vitre/vitre2.py")

	v4=get_display(arabic_reshaper.reshape("سد النافذَة د ليسر"))
	def fermer():
                Vitre.replique("SYNTHESE/Controler_les_vitres/Close_left_win.wav")
                os.system("python /home/PFA_ADAS/vitre/vitre3.py")

class VitreDroite(Vitre):
 pass


class SMS:
	def replique(path):
  		print(path)
  		os.system('omxplayer -o local '+path)
	s1=get_display(arabic_reshaper.reshape("صيفط ميساج"))
	def fct_SMS(data):
		self.replique("SYNTHESE/Gestion_sms/designer_le_nom.wav")

    		nom=get_display(arabic_reshaper.reshape("رضوان"))
		if nom in data:
			self.replique("SYNTHESE/Gestion_sms/confirmation_envoi_sms.wav")
                	os.system("python /home/PFA_ADAS/send_sms.py")

