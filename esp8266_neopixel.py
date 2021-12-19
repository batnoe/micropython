# Leds néopixels sur esp8266 d1 mini

import machine, neopixel
from time import *
import urandom

np = neopixel.NeoPixel(machine.Pin(4), 8)
val = 3

def randint(min, max):
    span = max - min + 1
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val

while True:
    for adresse_pixel in range(0, 8):
        r = randint(0, val)
        v = randint(0, val)
        b = randint(0, val)
        np[adresse_pixel] = (r, v, b)
        sleep_ms(125)
        np.write()

