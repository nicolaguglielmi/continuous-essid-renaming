# HC-SR04 Ultrasound Sensor
import time
from machine import Pin

# WeMos D4 maps GPIO2 machine.Pin(2) = TRIGGER
# WeMos D2 maps GPIO4 machine.Pin(4) = ECHO
triggerPort = 21
echoPort = 22

print("test")

trigger = Pin(triggerPort, Pin.OUT)
echo = Pin(echoPort, Pin.IN)
print("Ultrasonic Sensor. Trigger Pin=%d and Echo Pin=%d" % (triggerPort, echoPort))
trigger.off()
while True:
    # short impulse 10 microsec to trigger
    trigger.on()
    time.sleep_us(10)
    trigger.off()
    count = 0
    start = time.ticks_us() # get time in usec
    print(start)
    # Now loop until echo goes high
    while not echo.value():
        time.sleep_us(10)
        count += 1
        if count > 100:
            print("Counter exceeded")
            break
    duration = time.ticks_diff(start, time.ticks_us()) # compute time difference
    print(time.ticks_us())
    print("Duration: %f" % duration)

    # After 38ms is out of range of the sensor
    if duration > 38000 :
        print("Out of range")
        continue

    # distance is speed of sound [340.29 m/s = 0.034029 cm/us] per half duration
    distance = 0.017015 * duration
    print("Distance: %f cm" % distance)
    time.sleep(2)