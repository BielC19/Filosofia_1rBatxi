from machine import Pin, PWM
import time

buzzer = PWM(Pin(12))

buzzer.freq(17000)
buzzer.duty_u16(1000)
time.sleep(1)
buzzer.duty_u16(0)
