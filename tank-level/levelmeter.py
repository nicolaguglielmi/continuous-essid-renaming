#Anther POC of the idea to broadcast data through continuous ssid renaming
#Meter the level in a tank and broadcast the fill level
from hcsr04 import HCSR04
import time
import network

#set the trigger pin and the echo pin
trigger_pin=2
echo_pin=4

#tank diameter and height, in centimeters
radius=100
height=200

#pause between readings, in seconds:
readings=120

#configure the sensor wiring
sensor = HCSR04(trigger_pin=trigger_pin, echo_pin=echo_pin)

#service function to generate the network name
def essid_rename(value):
    essid=essid_base+str(value)
    ap_if.config(essid=essid, authmode=network.AUTH_WPA_WPA2_PSK, password='some random char 12345678900000**')
    ap_if.active(True)

#setup the wireles interface
ap_if = network.WLAN(network.AP_IF)

#configure a string for the essid base name
essid_base="Tank ABC:"

while True:
    distance = int(sensor.distance_cm())
    stock=((radius*radius*3.14)*(height-distance)/1000)
    print('Stock is:', stock, 'liters')
    essid_rename(stock)
    time.sleep(readings)

