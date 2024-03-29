
# import socket programming library 
import socket 
import json

# import thread module 
from _thread import *
import threading 
d={"d0":0,"d1":0,"d2":0,"d3":0,"d5":0}

print_lock = threading.Lock() 
  
# thread fuction 
def threaded(c): 
    while True: 
  
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
            c.close()
            # lock released on exit 
            print_lock.release() 
            break
  
        # reverse the given string from client 
        #data = data[::-1] 
        print(type(data))
        msg=json.loads(data.decode())
        d[msg["key"]]=msg["value"]
        c.send(json.dumps(d).encode())
        # send back reversed string to client 
        #c.send(data) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 