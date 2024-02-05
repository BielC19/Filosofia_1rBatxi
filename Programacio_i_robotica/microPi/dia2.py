from machine import Pin
import time

led1 = Pin(10, Pin.OUT)
led2 = Pin(11, Pin.OUT)
led3 = Pin(12, Pin.OUT)

while True:
    led1.value(1)
    time.sleep(0.2)
    led1.value(0)
    led2.toggle()
    time.sleep(0.2)
    led2.toggle()
    led3.toggle()
    time.sleep(0.2)
    led3.toggle()
    time.sleep(0.2)
    led3.toggle()
    led2.toggle()
    time.sleep(0.2)
    led2.toggle()
    led1.toggle()
    time.sleep(0.2)
    led3.toggle()