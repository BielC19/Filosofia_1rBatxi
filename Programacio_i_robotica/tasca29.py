#Fes un programa que donat un nombre per l'usuari faci totes les taules de multiplicar des del 2 fins a aquest nombre.
a = int(input("Digues fins a quin numero vol que et digui la taula: "))
a+=1

while True:
    if a>=2:
        for i in range(2, a):
            for n in range(1, 11):
                print(i, "*", n, "=", i*n, end=", ", sep="")
            print("\n")
        break               #aixo fa que el bucle es trenqui/com si la condicio es fes falsa 
    else:
        a = int(input("Introdueix un valor mes gran que 2: "))