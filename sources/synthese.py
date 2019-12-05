# -*- coding: utf-8 -*- 
#!/usr/bin/env python3
# GSEII3 _PFA_2019/2020

#-----------------------------------PARTIE SYNTHESE ------------------------------------------------------------------

###-----------------------------------IMPORT--------------------------------------------------------------------------

#Bibliotheque permettant la reconnaissance vocale en ligne et hors ligne
import speech_recognition as sr
# GTTS(Google Text-to-Speech)
from gtts import gTTS 

###-----------------------------------FONCTION------------------------------------------------------------------------

# fonction pour la synthese
def synthese(fct,file):
    print("text_to_speech_IN_ARABIC")

    fct=fct.decode("utf-8")
    #fct gtts permettant la convesion text to speech en arabe
    tts = gTTS(text=fct, lang='ar')
    #enragistrement du son sous format MP3
    tts.save(file+".mp3")
    print("done !!!!!!!")

# les repliques a synthetise
def mon_fichier(txt):
    #ouverture du fichier contetant les repliques
    file = open(txt+'.txt', "r")
    #lire toutes les repliques
    lines = file.readlines()
    file.close()
    return lines	

###---------------------------------------MAIN--------------------------------------------------------------------------
print("synthese ...............")
# a un competeur
a=1
#stockage des repliques dans la variable repliques
repliques=mon_fichier("rep_pfa")

#traitement de chaque replique
for replique in repliques:
    nom="rep"+str(a)
    print(replique)
    #fct de synthese
    synthese(replique,nom)
    a=a+1
	
###-----------------------------------FIN SYNTHESE-----------------------------------------------------------------------
