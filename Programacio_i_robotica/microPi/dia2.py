from machine import Pin
import time

led = Pin(10, Pin.OUT)
led2 = Pin(11, Pin.OUT)
led3 = Pin(12, Pin.OUT)

while True:
    led.toggle()
    led2.toggle()
    led3.toggle()
    time.sleep(1)