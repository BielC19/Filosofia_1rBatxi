#Escriu un programa en Python que utilitzi un bucle for i la funció range() per calcular la suma dels quadrats dels números parells de l'1 al 50. 
#No obstant això, només has de sumar el quadrat si és major de 100
import math
b = 0
for n in range(0, 51, 2):
    b = b + (n**2)
    print(b)