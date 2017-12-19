# Prototype of a P2P messaging application
# Created 12.18.2017

import socket
import sys
import time

class Host:
    def __init__(self):
        s = socket.socket()
        host = socket.gethostbyname(socket.gethostname())
        print(host)
        port = 10000
        s.bind((host, port))
        print('waiting for connection...')
        s.listen(1)
        conn, addr = s.accept()
        print(addr, "has connected")  

        while True:
            try:
                message = input('>>> ').encode()
                conn.send(message)

                incoming = conn.recv(1024)
                print(incoming.decode())
            except KeyboardInterrupt:
                sys.exit(0)
                
class Guest:
    def __init__(self):
        s = socket.socket()
        host = input('Hostname: ')
        port = 10000
        s.connect((host,port))

        while True:
            try:
                incoming = s.recv(1024)
                print(incoming.decode())

                message = input('>>> ').encode()
                s.send(message)
            except KeyboardInterrupt:
                sys.exit(0)
                
relationship = None
while True:
    relationship = input('Will you be host or guest? ')
    if relationship == 'host' or relationship == 'guest':
        break
    else:
        print('Invalid response.')

if relationship == 'host':
    host = Host()
else:
    guest = Guest()
    
