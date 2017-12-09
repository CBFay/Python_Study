# https://www.youtube.com/watch?v=DIPZoZheMTo
# simple server that sends back whatever we send to it

import socket
import threading

# AF_INET means IPv4, and SOCK_STREAM means TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 10000)) # an address and a port

sock.listen(1) # the amount of parenting connections we want to allow

connections = []

def handler(c):
    global connections
    while True: # this is called a blocking function
        data = c.recv(1024) 
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close
            break

while True:
    c, a = sock.accept() # returns the connection, and address
    cThread = threading.Thread(target=handler, args=(c,a)) # create a new thread for the new connection. Handler is the name of the function that handles the connection
    cThread.daemon = True # means the program can close even if there are still threads running
    cThread.start()
    connections.append(c)
    print(connections)
