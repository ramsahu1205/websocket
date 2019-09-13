import socket
import json

d={"d0":0,"d1":0,"d2":0,"d3":0,"d5":0}
connUser={}
HOST = '192.168.0.105'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        connUser[addr]=True
        with conn:
            print('Connected by', addr)
            while connUser[addr]:

                data = conn.recv(1024)
                if not data:
                    connUser[addr]=False
                else:
                    print(type(data))
                    msg=json.loads(data.decode())
                    d[msg["key"]]=msg["value"]
                    conn.send(json.dumps(d).encode())
                print(connUser)
            conn.close()
            print("conn close")