#An idea to broadcast some promotional messages through continuous ssid renaming, fill the messages.txt with your messages
import machine
import time
import network

#set the messages file
mess_file='messages.txt'

#service function to generate the network name
def essid_rename(message):
    ap_if.config(essid=message, authmode=network.AUTH_WPA_WPA2_PSK, password='some random char 12345678900000**')
    ap_if.active(True)

#setup the wireles interface
ap_if = network.WLAN(network.AP_IF)

file_handler=open(mess_file)
messages=file_handler.read().split('\n')
file_handler.close()

for i in messages:
    data=i.split('\t')
    timing=int(data[0])
    essid=str(data[1])
    essid_rename(essid)
    time.sleep(timing)