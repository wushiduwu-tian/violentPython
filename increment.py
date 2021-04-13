#! /bin/python3 

import socket 

s = socket.socket()
s.connect(("ad.samsclass.info", 10203))
string = s.recv(1024).decode()
print(string)
number = string[-3:]
print(number)
number = int(number) + 1 
s.send(str(number).encode()) 
print(s.recv(1024).decode())
s.close() 
