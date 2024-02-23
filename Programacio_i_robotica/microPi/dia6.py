from machine import Pin, PWM
import utime


def main():

    
    #Configura el Servo de 360
    servo_360 = PWM(Pin(8))
    servo_360.freq(50)
    
    pulsador = Pin(12, Pin.IN)
    
    while True:
        if pulsador == 0:
            angulo = float(input('Ingrese un ángulo: '))
            duty = int((12.346*angulo**2 + 7777.8*angulo + 700000))
            servo_360.duty_ns(duty)
    
    
if __name__ == '__main__':
    main()