# tcp_server.py
# a simple tcp server

import socket

# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket object to an address.
ip = socket.gethostbyname(socket.gethostname())
port = 1236 # any 4 digit integer
address = (ip,port)

server.bind(address)

# start listening for connections
server.listen(1) # this argument specifies how many connections we can have at once

print('[*] Started listening on ',ip,':',port)

client, addr = server.accept()
print('[*] Connection from ',addr[0],':',addr[1])
while True:
    data = client.recv(1024) # buffer size
    print('[*] Received ',data.decode(),' from the client')
    print("\tProcessing data")
    if data.decode() == 'Hello server':
        client.send('Hello client'.encode('utf-8'))
        print("\tProcessing done. \n[*] Reply sent")
    elif data.decode() =='disconnect':
        client.send('Goodbye'.encode('utf-8'))
        client.close()
    else:
        client.send('Invalid data'.encode('utf-8'))
        print("\tProcessing done. Invalid data. \n[*] Reply sent")
