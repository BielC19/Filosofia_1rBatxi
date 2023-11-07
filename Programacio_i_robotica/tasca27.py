#Escriu un programa en Python que utilitzi un bucle for i la funció range() per calcular la suma dels quadrats dels números parells de l'1 al 50. 
#No obstant això, només has de sumar el quadrat si és major de 100
import math
b = 0
for n in range(0, 51, 2):
    if n**2 < 100:
        b += n**2

print(f"La suma de tots els quadrats es exepte els menors de 100: {b}")