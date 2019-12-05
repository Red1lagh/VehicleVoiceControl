# -*- coding: utf-8 -*- 
#!/usr/bin/env python3
# GSEII3 _PFA_2019/2020

#-----------------------------------PARTIE RECONNAISSANCE ------------------------------------------------------------------

###-----------------------------------IMPORT--------------------------------------------------------------------------

#Bibliotheque permettant la reconnaissance vocale en ligne et hors ligne
import speech_recognition as sr
#time
import time
#d’interfacer avec le système d’exploitation
import os
#module pour la reproduction des sons
from playsound import playsound

###-----------------------------------FONCTION------------------------------------------------------------------------

#fonction des repliques
def replique(path):
    print(path)
    #fct pr lancer les repliques
    os.system(r'start '+path)

#fonction de reconnaissance-----------
def recordAudio():
    # enregistrement Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        #recording
        audio = r.listen(source)

    # Speech recognition en utilisant Google Speech Recognition 
    data = ""
    try:
        data=(r.recognize_google (audio, language = "ar-AR")).encode('utf-8')
        print("You said: " + data)
    #gestion des exception
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

# fonction des commandes--------------
def fct_principales(data):
    #fct d'eclairage du code
    if "تشغيل ضوء التقابل" in data:
        replique(".\\synthese\\Eclairage_code\\rep_activ_code.mp3")
        time.sleep(30)
        replique(".\\synthese\\Eclairage_code\\rep_desac_code.mp3")
    #fct d'activation d'eclairage du phare
    if "تشغيل ضوء الطريق" in data:
        replique(".\\synthese\\Eclairage_phare\\rep_activ_phare.mp3")
    #fct de desactivation d'eclairage du pahre
    if "ايقاف ضوء الطريق" in data:
        replique(".\\synthese\\Eclairage_phare\\rep_desac_phare.mp3")
    #fct d'activation d'eclairage du signal droit
    if "تشغيل ضوء تغيير الإتجاه الايمن" in data:
        replique(".\\synthese\\Eclairage_signal\\signal_droit\\rep_activ_sigd.mp3")
        time.sleep(30)
        replique(".\\synthese\\Eclairage_signal\\signal_droit\\rep_desac_sigd.mp3")
    #fct d'activation d'eclairage du signal gauche
    if "تشغيل ضوء تغيير الإتجاه الأيسر" in data:
        replique(".\\synthese\\Eclairage_signal\\signal_gauche\\rep_activ_sigg.mp3")
        time.sleep(30)
        replique(".\\synthese\\Eclairage_signal\\signal_gauche\\rep_desac_sigg.mp3")


###---------------------------------------MAIN--------------------------------------------------------------------------
#msg d'acceuil
replique("bonjour.mp3")

while 1:
    #fct de recording
    data = recordAudio()
    #fct de commande
    fct_principales(data)
  
#-----------------------------------PARTIE RECONNAISSANCE ------------------------------------------------------------------