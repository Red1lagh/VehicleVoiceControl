# -*- coding: utf-8 -*- 
#!/usr/bin/env python3

import speech_recognition as sr
from gtts import gTTS

def synthese(fct,file):
    print("text_to_speechh")
    tts = gTTS(text=fct, lang='ar')
    tts.save(file+".mp3")
    print("doneeeeeee")

def mon_fichier(txt):
    file = open(txt+'.txt', "r")
    lines = file.readlines()
    file.close()
    return lines	

 
print("synthese ...............")
a=1
repliques=mon_fichier("rep_pfa")
for replique in repliques:
    nom="rep"+str(a)
    print(replique)
    synthese(replique,nom)
    a=a+1
