import websocket
import json
null = None
d={
   "sid": "rfid-f938f464-d0b2-48b1-9741-acd69007aef2",
   "request": False,
   "bgtb": [
      {
         "id": "rfid-ba6f59d8-0e10-49d4-998c-3923a6a47ff9",
         "session_id": "rfid-11c44def-f4f4-46f7-b190-3814ccd14f2f",
         "referrer": "https://testease.linq.app/linq/5702?listingId=5702&private=true&utm_source=QR%20Code&utm_medium=Offline",
         "latitude": null,
         "longitude":null,
         "device": {
            "browserName": "Chrome",
            "browserVersion": "76.0.3809.132",
            "oSName": "Android",
            "oSVersion": "6.0",
            "deviceVendor": "LG",
            "deviceModel": "Nexus 5",
            "userAgentRaw": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"
         },
         "url": "https://testease.linq.app/linq/5702?listingId=5702&private=true&utm_source=QR%20Code&utm_medium=Offline#LoginDone",
         "listing_id": 5702,
         "origin": "web-private",
         "added_to_home_screen": False,
         "mobile": "9031144771",
         "eventTime": "2019-09-22T19:22:12",
         "event": {
            "event": "rfid",
            "event_category": "rfid",
            "event_label": "rfid",
            "private": True,
            "eventTime": "2019-09-22T19:22:12"
         },
         "utm_source": "",
         "utm_medium": "",
         "utm_campaign": ""
      }
   ]
}
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###".encode())

def on_open(ws):
    def run(*args):
        for i in range(2):
            global d 
            time.sleep(1)
            print(i)
            if i==1:
                d={
                    "sid": "e411e953-5d00-4ed7-a7d0-bba699c1c903", 
                    "request":True
                }
            tempd=json.dumps(d)
            print(tempd)
            ws.send(json.dumps(d))
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://mylinq.in:8081/wsee",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()