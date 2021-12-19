import machine, time, bme280, os
from ssd1306 import SSD1306_I2C
from pyb import delay, LED

i2c = machine.SoftI2C(scl=machine.Pin('Y9'), sda=machine.Pin('Y10'))
bme = bme280.BME280(mode=bme280.BME280_OSAMPLE_2, address=0x77, i2c=i2c)

i2c = machine.SoftI2C(sda=machine.Pin("Y8"), scl=machine.Pin("Y6"))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

i = 0 #os.chdir("Volumes/Mac-OS/Users/bernardpetit")
fich = 'p'
fichier = open(fich, 'w')

while True:
    i += 1
    temperature, pression, humidite = bme.values
    pression = str(float(pression[:6])+21)
    temperature = str(float(temperature[:4])+1) + "C"
    fichier.write(pression + ",")

    oled.fill(0) # efface l'ecran
    oled.text(str(i) + " Mesures", 10, 0)
    oled.text("Temp :", 0, 15)
    oled.text(temperature, 50, 15)
    oled.text("Humi :", 0, 25)
    oled.text(humidite, 50, 25)
    oled.text("Pres :", 0, 35)
    oled.text(pression , 50, 35)
    oled.show()
    LED(1).on()
    time.sleep(0.25)
    LED(1).off()
    time.sleep(600)

