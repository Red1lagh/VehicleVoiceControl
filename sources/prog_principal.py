# -*- coding: utf-8 -*-

#!/usr/bin/env python3

from MyClass import *


GPIO.setmode(GPIO.BCM)
# led  code
GPIO.setup(9, GPIO.OUT)
# led  phare
GPIO.setup(11, GPIO.OUT)


a = Audio()
e = Eclairage()
g = Essuies_glaces()
v = Vitre()
s = SMS()
os.system('omxplayer -o local /home/PFA_ADAS/SYNTHESE/bonjour.wav')

while 1:

    data = a.recordAudio()
    if e.c11 in data or e.c12 in data or e.c13 in data or e.c14 in data:
        e.activer_phare()
    if e.c21 in data or e.c22 in data or e.c23 in data or e.c24 in data:
        e.desactiver_phare()
    if e.c31 in data or e.c32 in data or e.c33 in data or e.c34 in data:
        e.activer_code()
    if e.c41 in data or e.c42 in data:
        e.desactiver_code()
    if e.c4 in data:
        e.signal_droit()
    if e.c5 in data:
        e.signal_gauche()

    if g.g1 in data:
        g.activer_essuies_glaces()
    if g.g2 in data:
        g.essuie_glaces_vitesse1()
    if g.g3 in data:
        g.essuie_glaces_vitesse2()
    if g.g4 in data:
        g.essuie_glaces_top_vitesse()
    if g.g5 in data:
        g.desactiver_essuies_glaces()

    if v.v1 in data:
        v.ouvrir()
    if v.v2 in data:
        v.vitre_niv1()
    if v.v3 in data:
        v.vitre_niv2()
    if v.v4 in data:
        v.fermer()

    if s.s1 in data:
        s.fct_SMS()
