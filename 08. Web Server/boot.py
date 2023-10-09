# https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/


# We create our web server using sockets and the Python socket API.
# The official documentation imports the socket library as follows:
try:
    import usocket as socket
except:
    import socket

# We need to import the Pin class from the machine module to be able to
# interact with the GPIOs.
from machine import Pin

# The network library allows us to connect the ESP32 to a Wi-Fi network.
import network

# The following lines turn off vendor OS debugging messages:
import esp
esp.osdebug(None)

# Run a garbage collector:
#     A garbage collector is a form of automatic memory management.
#     This is a way to reclaim memory occupied by objects that are no longer
#     in use by the program. This is useful to save space in the flash memory.
import gc
gc.collect()

# The following variables hold your network credentials so that the ESP is
# able to connect to your router:
ssid = 'MovistarFibra-97FE30'
password = 'unafacil23'

# Set the ESP32 as a Wi-Fi station:
station = network.WLAN(network.STA_IF)

# Activate the station and connects to your router using the SSID and password
# defined earlier:
station.active(True)
station.connect(ssid, password)

# The following statement ensures that the code doesn’t proceed while the ESP
# is not connected to your network:
while station.isconnected() == False:
    pass

# After a successful connection, print network interface parameters like the
# ESP32 IP address – use the ifconfig() method on the station object: 
print('Connection successful')
print(station.ifconfig())

# Create a Pin object called led that is an output, that refers to the
# ESP32 GPIO2:
led = Pin(2, Pin.OUT)
