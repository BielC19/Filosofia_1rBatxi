#Trobar el nombre més gran i també el més petit en una llista donada per l'usuari.
#Fer-ho amb for primer i després amb while.

llista = []
b = int(input("Quant numeros vols comprocar: "))
for a in range(b):
    noms = input("Introdueix un numero: ")
    llista.append(noms)
    a += 1
