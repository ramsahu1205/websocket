import socket                
import json
import time
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
#s.connect(('192.168.0.105', port))
s.connect(('testease.linq.app',8081)) 
#d={"key":"d0","valclsue":1}
d={
  "sid": "e411e953-5d00-4ed7-a7d0-bba699c1c903", 
  "request":True
}
s.send(json.dumps(d).encode())
print(s.recv(1024).decode())
s.close()  