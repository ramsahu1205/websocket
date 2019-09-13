import socket                
import json
import time
# Create a socket object 
       
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
#s.connect(('192.168.0.105', port)) 
# receive data from the server 
while True:
   # s.connect(('192.168.0.105', port))
    s = socket.socket()  
    s.connect(('192.168.0.105', port))
      
    d={"key":"d5","value":1}
    s.send(json.dumps(d).encode())
    print(s.recv(1024).decode())
    s.close()  
    #s.close() 
    time.sleep(5)
# close the connection 
