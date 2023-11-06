#Escriu un programa en Python que prengui una llista de números (escrita manualment) 
#com a entrada i trobi els nombres parells i senars en aquesta llista.

#Emmagatzema els nombres parells en una llista separada anomenada "parells" 
#i els nombres senars en una altra llista separada anomenada "senars".
#Imprimeix les llistes de parells i senars per mostrar els resultats

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = 0
numeros = []
while a != 10:
    b = int(input("Introdueix un numero: "))
    numeros.append(b)
    a += 1
print(numeros)
parells = []
senars = []
for n in numeros:
    n -= 1
    if n % 2 == 0:
        parells.append(numeros[n])
    else:
        senars.append(numeros[n])
print(parells)
print(senars)