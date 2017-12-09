# An elementary TCP client
# https://www.youtube.com/watch?v=SepyXsvWVfo

import socket

# socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP oriented socket

# get the IP address of a server
ip=socket.gethostbyname('www.google.com')
print(ip)

port=80

#the address is a tuple binding of the IPv4 address and the port
address=(ip,port) # the address of the server we're going to connect to

# connect to the server
client.connect(address)

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") # this is valid data

received = client.recv(1024) # receive data, receives buffer size
print(received)
