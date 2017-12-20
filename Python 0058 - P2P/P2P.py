# Usernames
# Internet?
# Combine objects
# Refactor

import socket
import threading
import sys
import time

class Host:
    def __init__(self):
        self.exit = ['*Disconnected*\n', '\n*Disconnected*\n']
        self.name = input('Name? ')
        self.s = socket.socket()
        self.address = socket.gethostbyname(socket.gethostname())
        print('Your address:', self.address)
        self.port = 10000
        self.s.bind((self.address, self.port))
        print('waiting for connection...')
        self.s.listen(1)
        
        try:
            self.conn, self.guest = self.s.accept()
        except KeyboardInterrupt:
            print('\n'+self.exit[0])
            sys.exit(0)
            
        print(self.guest, "has connected")
        self.exchange()
                
    def talk(self):
        while True:
            outgoing = (self.name + ': ' + input()).encode()
            self.conn.send(outgoing)
        
    def listen(self):
        while True:
            incoming = self.conn.recv(1024)
            print(incoming.decode())
            if not incoming:
                self.conn.close()
                print(self.exit[0])
                sys.exit(0)
                
    
    def exchange(self):
        talker = threading.Thread(target=self.talk)
        listener = threading.Thread(target=self.listen)
        
        talker.daemon = True
        listener.daemon = True
        
        listener.start()
        talker.start()
            
        try:
            listener.join()
        except KeyboardInterrupt:
                self.conn.close()
                print(self.exit[1])
                sys.exit(0)
                
class Guest:
    def __init__(self):
        self.exit = ['*Disconnected*\n']
        self.name = input('Name? ')
        self.address = socket.gethostbyname(socket.gethostname())
        print('Your address:',self.address)
        self.s = socket.socket()
        self.hostaddress = input('Host address: ')
        self.port = 10000
        self.s.connect((self.hostaddress, self.port))
        print('Connected!')
        self.exchange()

    def talk(self):
        while True:
            outgoing = (self.name + ': ' + input()).encode()
            self.s.send(outgoing)
        
    def listen(self):
        while True:
            incoming = self.s.recv(1024)
            print(incoming.decode())
            if not incoming:
                self.s.close()
                print(self.exit[0])
                sys.exit(0)
                
    
    def exchange(self):
        talker = threading.Thread(target=self.talk)
        listener = threading.Thread(target=self.listen)
        
        talker.daemon = True
        listener.daemon = True
        
        listener.start()
        talker.start()

        try:
            listener.join()
        except KeyboardInterrupt:
                self.s.close()
                print(self.exit[1])
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
    
