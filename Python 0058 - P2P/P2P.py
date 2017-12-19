# Prototype of a P2P messaging application
# Created 12.18.2017

import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        myaddress = socket.gethostbyname(socket.gethostname())
        print('My IPv4 address:', myaddress)
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)
        
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                self.connections.remove(c)
                c.close
                print(str('{} : {} disconnected'.format(a[0], a[1])))
                break
    
    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str('{} : {} connected'.format(a[0], a[1])))

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def __init__(self, address):
        self.sock.connect((address, 10000))
        
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))    
        
    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

            
if(len(sys.argv)) > 1:
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()

        
