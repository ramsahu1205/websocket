import socket                
import json
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('192.168.0.105', port)) 
# receive data from the server 
d={"key":"d5","value":1}
s.send(json.dumps(d).encode())
print(s.recv(1024).decode()) 
# close the connection 
s.close()  