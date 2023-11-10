#Trobar el nombre més gran i també el més petit en una llista donada per l'usuari.
#Fer-ho amb for primer i després amb while.

llista = []
b = int(input("Quant numeros vols comprocar: "))
for a in range(b):
    noms = int(input("Introdueix un numero: "))
    llista.append(noms)
    a += 1

c = 0
for i in llista:
    if i > c:
        c = i
print(c)

d = llista[0]
for i in llista:
    if i > d:
        d = i
print(d)