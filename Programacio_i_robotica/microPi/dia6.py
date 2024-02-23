from machine import Pin, PWM
import time

#Configura el Servo de 360
servo_360 = PWM(Pin(8))
servo_360.freq(50)

pulsador = Pin(12, Pin.IN)

while True:
    print(pulsador.value())
    time.sleep(0.1)
    if pulsador.value() == 0:
        angulo = float(input('Ingrese un ángulo: '))
        if angulo >= 0 and angulo <= 190:
            if angulo == 45:
                print("Calibrat")
            duty = int((12.346*angulo**2 + 7777.8*angulo + 700000))
            servo_360.duty_ns(duty)
