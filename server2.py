
import ConnectWifi
import socket

ConnectWifi.connect()

data = "Test envoi serveur"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(12)

while True:
    (conn, addr) = s.accept()
    print('Accept la connection de %s' % str(addr))
    conn.sendall(data)
    conn.close()
