#Sol·licita a l'usuari que ingressi una llista de 5 nombres enters positius (els nombres s'introduiran d'un en un).
#Comprova si el nombre d'entrada és més gran que 10; en cas contrari, repeteix fins que escrigui un nombre més gran que 10.
#Permet a l'usuari triar entre calcular la suma o el producte dels nombres introduïts.
#Imprimeix la suma o el producte, segons l'opció triada per l'usuari.
#Després de processar la llista, pregunta a l'usuari si desitja fer una altra operació o sortir del programa. 
#Si l'usuari decideix fer una altra operació, sol·licita una nova llista de nombres.
llista5num = []
for n in range(5):
    a = int(input("Introdueix un numero: "))
    b = True
    while b:
        if a <= 10:
            a = int(input("Introdueix un valor mes gran que 10: "))
        else:
            b = False
    llista5num.append(a)
print(llista5num)