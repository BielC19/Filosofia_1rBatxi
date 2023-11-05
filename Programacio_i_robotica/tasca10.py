#Fes un programa que donat un enter com 145521, el mostri per pantalla com si fos una hora en el format HH:MM:SS. El format de sortida ha de tenir dos punts entre hora, minuts i segons. En un cas com 5 minuts i 3 segons s'accepta 5:3:0.
dades = int(input("Introdueix l'hora en HHMMSS : "))
hora = int(dades/10000)
minuts = int((dades/100)%100)
segons = int(dades%100)
print(f"L'hora que has introduit es: \n{hora}:{minuts}:{segons}")