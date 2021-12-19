# Ecrit ton programme ici ;-)
import esp32, utime

while True:
    print(esp32.hall_sensor())
    utime.sleep_ms(500)
