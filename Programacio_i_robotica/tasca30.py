#Un nombre x es denomina "perfecte" si la suma dels seus divisors menors que x coincideix precisament amb x. 
#Exemples de nombres perfectes són el 6 (1 + 2 + 3) i el 28 (1 + 2 + 4 + 7 + 14). 
#Descobreix quins nombres perfectes n'hi ha que siguin menors que el nombre que introdueixi l'usuari.
a = int(input("Posa el numero per comprovar si es perfercte: "))
llista_de_valors=[]
b = 0
for i in range(2, a):
    for n in range(i):
        n+=1
        if (i%n) == 0:
            b += n

    llista_de_valors.append(b)
    b=0
for i in llista_de_valors:
    if a < i:
        llista_de_valors.remove(i)

print(f"els teus valor perfectes son {llista_de_valors}")