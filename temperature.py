# Ecrit ton programme ici ;-)
from microbit import *

temp = 0

while True:
    if button_a.was_pressed():
        temp = temp - 1
        display.scroll(temperature() + temp)
        pin0.write_digital(0)
    elif button_b.was_pressed():
        temp = temp + 1
        display.scroll(temperature() + temp)
        pin0.write_digital(1)
    else:
        display.scroll(temperature() + temp)
