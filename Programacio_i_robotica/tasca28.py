#Trobar el nombre més gran i també el més petit en una llista donada per l'usuari.
#Fer-ho amb for primer i després amb while.
a = 0
llista = []
b = int(input("Quant numeros vols comprocar: "))
while a!=b:
    noms = input("Introdueix un numero: ")
    llista.append(noms)
    a += 1
def maxim(valors):
