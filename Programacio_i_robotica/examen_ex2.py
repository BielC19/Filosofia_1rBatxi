#Fer un programa que donada una dada numèrica en aquest format: ABCD. Faci el següent
#funcionament:
#1- Extreure cada una de les dades A,B,C i D i mostrar-ho a l’usuari.
#2- Calcular el caràcter de la taula ASCII equivalent +50 a cada una de les dades i
#mostrar-ho a l’usuari.
#3- Demana a l’usuari l’inicial del nom i del primer cognom (en majúscules) i codifica’l
#utilitzant la taula ASCII amb el següent mode d’encriptació:
#● Valor numèric ASCII del caracter - 10
#4- Mostrar a l’usuari els caràcters encriptats amb els caràcters d’ASCII nous.

#1
lletres = "ABCD"
lletra_a_lletra = []
for lletra in lletres:
    lletra_a_lletra.append(lletra)

print(lletra_a_lletra)

#2
lletra_a_lletra_ascii = []
for caracter in lletra_a_lletra:
    lletra_a_lletra_ascii.appened(ord(caracter + 50))
