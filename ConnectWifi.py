def connect():
    import network

    ip        = '192.168.8.10'
    subnet    = '255.255.255.0'
    gateway   = '192.168.8.1'
    dns       = '192.168.8.1'
    ssid      = ""
    password  =  ""

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return

    station.active(True)
    station.ifconfig((ip,subnet,gateway,dns))
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("Connection successful")
    print(station.ifconfig())

def disconnect():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)
