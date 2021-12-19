import time, machine, onewire, esp_ds18x20

# DQ = broche 26 (D2)
data = machine.Pin(26)

# creation objet onewire
ds = esp_ds18x20.DS18X20(onewire.OneWire(data))

# Scan le bus OneWire et recupere l'ID de chaque sonde
adresses_cpt = ds.scan()
print('Adresses capteurs trouvées:', adresses_cpt)

# Lecture et affichage température de chaque sonde
while True:
    print('temperatures:', end=' ')
    ds.convert_temp()
    for adresse in adresses_cpt:
        print(ds.read_temp(adresse), end=' ')
    print()
    time.sleep_ms(1000)
