import socket                
import json
import RPi.GPIO as GPIO
import time
# Create a socket object 
s = socket.socket()          
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) 
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
while true:
# receive data from the server 
    d={"key":"d5","value":1}
    s.send(json.dumps(d).encode())
    od=s.recv(1024).decode()
    print(d)
    if od["d0"]==1:
        GPIO.output(18, GPIO.HIGH)
        print("device 1 is connected")
    else:
        GPIO.output(18,GPIO.LOW)
        print("device 1 disconnected")
    time.sleep(4) 

# close the connection 
s.close()  