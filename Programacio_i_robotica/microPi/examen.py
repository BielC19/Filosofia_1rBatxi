from machine import Pin, PWM
from time import sleep


led_pins = [10, 11]
led_pins2 = [11, 10]

servo_360 = PWM(Pin(8))
servo_360.freq(50)

leds = [Pin(pin, Pin.OUT) for pin in led_pins]
leds2 = [Pin(pin, Pin.OUT) for pin in led_pins2]

pulsador = Pin(12, Pin.IN)


while True:
    if pulsador.value() == 0:
        for i in range(len(leds)):
            leds[i].value(1)
            sleep(0.2)
            leds[i].value(0)
    else:
        duty = int((12.346*90**2 + 7777.8*90 + 700000))
        servo_360.duty_ns(duty)
        servo_360.duty_ns(-duty)

