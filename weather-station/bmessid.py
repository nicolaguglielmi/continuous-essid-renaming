#An idea to broadcast some weather data as a wifi essid
import machine
import BME280
import time
import network

#set the rate of data refresh, in seconds
refreshtime=60

# ESP32 - Pin assignment
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=10000)

#setup wireles interface
ap_if = network.WLAN(network.AP_IF)

while True:
    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature
    humi = bme.humidity
    pres = bme.pressure
    print("_____________________")
    print("Temperature :",temp)
    print("Humidity    :",humi)
    print("Pressure    :",pres)
    print("_____________________")
    essid='Temp:'+temp+" Humi:"+humi+" Pres:"+pres
    ap_if.config(essid=essid, authmode=network.AUTH_WPA_WPA2_PSK, password='some random char 12345678900000**')
    ap_if.active(True)
    time.sleep(60)