
# distance ultrason HC-SR04

from machine import Pin
import hcsr04, time

# pin_echo : pin pour mesurer la distance
# pin_trig : pin pour envoyer les impulsions

pin_echo = 4  # sortie D2 --> GPIO04
pin_trigger = 5  # sortie D1 --> GPIO05
pin_lettre = 12 # d6 lettre led verte
pin_colis = 14  # d5 colis led rouge

# initialisation librairie HC-SR04
hc_sr04 = hcsr04.HCSR04(pin_echo, pin_trigger)
lettre = Pin(pin_lettre, Pin.OUT)
colis = Pin(pin_colis, Pin.OUT)

while True:
    distance = hc_sr04.lecture_distance()
    #print (distance)
    if (distance > 50): #== -1):
        #print ("Mesure superieure a 4 metres")
        colis(0)
        lettre(0)
    elif (distance < 20):
        #print ((distance), "cm")
        colis(1)
        lettre(0)
    elif (distance > 20 and distance < 50):
        print ((distance), "cm")
        lettre(1)
        colis(0)
    #time.sleep(0.5)
