from wifi_manager import WifiManager
from time import sleep

wm = WifiManager()
wm.connect()

while True:
    if wm.is_connected():
        print("Connected!")
    else:
        print("Disconnected!")
    sleep(1)
