from machine import Pin
from time import sleep

led1 = Pin(10, Pin.OUT)
led2 = Pin(11, Pin.OUT)
led3 = Pin(12, Pin.OUT)

led_pins = [10, 11, 12, 13]
led_pins2 = [13, 12, 11, 10]

leds = [Pin(pin, Pin.OUT) for pin in led_pins]
leds2 = [Pin(pin, Pin.OUT) for pin in led_pins2]


while True:
    for i in range(len(leds)):
        leds[i].value(1)
        sleep(0.2)
    for i in range(len(leds2)):
        leds[i].value(0)
        sleep(0.2)
    for i in range(len(leds)):
        leds2[i].value(1)
        sleep(0.2)
    for i in range(len(leds2)):
        leds2[i].value(0)
        sleep(0.2)

'''
while True:
    led1.value(1)
    sleep(0.2)
    led1.value(0)
    led2.value(1)
    sleep(0.2)
    led2.value(0)
    led3.value(1)
    sleep(0.2)
    led3.value(0)'''