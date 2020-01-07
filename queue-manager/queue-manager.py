#a POC of  queue manager with two button to increment and decrement the current value and broadcast it by wifi
import machine
from machine import I2C, Pin
import time
import network


#set to True to enable a display, False to disable it
use_display=True

if use_display:
    #display setup, i have a 128x32 oled on this board, tune the values to your display
    import ssd1306
    rst = Pin(16, Pin.OUT)
    rst.value(1)
    scl = Pin(5, Pin.OUT, Pin.PULL_UP)
    sda = Pin(4, Pin.OUT, Pin.PULL_UP)
    i2c = I2C(scl=scl, sda=sda, freq=450000)
    oled = ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

#service function to redraw a display with a string
def draw_display(text):
    if use_display:
        oled.fill(0)
        oled.text(str(text),5,15)
        oled.show()
    else:
        print('You are at:', counter)

#service function to generate the network name
def essid_rename(actual_counter):
    essid=essid_base+str(actual_counter)
    ap_if.config(essid=essid, authmode=network.AUTH_WPA_WPA2_PSK, password='some random char 12345678900000**')
    ap_if.active(True)

#setup the button up to pin 12
button_up = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

#setup the button down to pin 0
button_down = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

#seconds of sleep between consecutive button press, to avoid multiple readings
button_pause=0.1

#counter value
counter=0

#combo button status, to avoid increment and decrement counter after a combo pressure
combo=False

#setup wireles interface
ap_if = network.WLAN(network.AP_IF)

#configure a string for the essid base name
essid_base="It's the turn of:"

#just clean the oled
draw_display("Press a button")
print("Press a button...")

#let's start an infinite loop to keep checking the status of the buttons
while True:
    #reset function, pressing both buttons will reset the counter to 0
    if not button_up.value() and not button_down.value():
        print('Combo Button pressed!', counter)
        counter=0
        combo=True
        draw_display('Reset complete')
        time.sleep(2)
        draw_display('We serve:'+str(counter))
        essid_rename(counter)
    if not button_up.value() and not combo:#up button counter
        counter+=1
        print('Button up pressed!', counter)
        draw_display('We serve:'+str(counter))
        essid_rename(counter)
        time.sleep(button_pause)
    if not button_down.value() and not combo:#down button counter plus negative number check
        if counter>0:
            counter-=1
        else:
            counter=0
        print('Button down pressed!', counter)
        draw_display('We serve:'+str(counter))
        essid_rename(counter)
        time.sleep(button_pause)
    #reset combo button status
    combo=False