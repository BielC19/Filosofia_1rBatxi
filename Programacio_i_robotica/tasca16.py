#Avaluar les següents expressions amb diferents valors de a,b i c (a i b tipus int, c tipus string) i explica els problemes que trobes.

a = int(input("introdueix el primer numero:"))
b = int(input("introdueix el segon numero:"))
c = input("introdueix una lletra:")

print(c != 'a' or c != 'b')         #Si la lletre que li dones a la variable c no es 'a' o no es 'b' et dona True es compleix sempre
print(a < 1 or a > -1)              #Si el valor de a es mes petit que 1 o es mes gran que -1 es compoleix sempre
print(c != 'a' or c == 'a')         #Si la lletra que demanes a la variable c es diferent a 'a' o iugal que 'a' es compleix sempre
print(b < a or b > a)               #Si el valor de b es mes petit que el que a o b es mes gran que a aixi que es compleix sempre que no siguin iguals els dos valors
