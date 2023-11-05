#Donat qualsevol nombre enter, en fer-ne la divisió entera per 10, en perds una xifra.
#Utilitzant aquesta idea, fes un programa que llegeixi un número i et digui quantes xifres té.
#Es considera que el 0 també té una xifra

numero = abs(int(input("Introdueix un nombre: ")))
n = 0
if numero==0:
    print("El numeo de numeros que has introduit es 1")
else:
    while numero!=0 or numero<0:
        numero = numero//10
        n += 1
    print(f"El teu numero de numeros es {n}")