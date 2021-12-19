#
import machine, neopixel
from time import *
from random import randint

val = 20
np = neopixel.NeoPixel(machine.Pin(27), 8)

while True:
    for adresse_pixel in range(0, 4):
        r = randint(0, val)
        v = randint(0, val)
        b = randint(0, val)
        np[adresse_pixel] = (r, v, b)
        np.write()
        sleep_ms(100)
