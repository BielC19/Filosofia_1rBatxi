#Escriu un programa en Python que prengui una llista de números (escrita manualment) 
#com a entrada i trobi els nombres parells i senars en aquesta llista.

#Emmagatzema els nombres parells en una llista separada anomenada "parells" 
#i els nombres senars en una altra llista separada anomenada "senars".
#Imprimeix les llistes de parells i senars per mostrar els resultats

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
parells = []
senars = []
for n in numeros:
    if n % 2 == 0:
        parells.append(numeros[n-1])
    else:
        senars.append(numeros[n-1])
print(parells)
print(senars)