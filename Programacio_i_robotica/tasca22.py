#Crea una calculadora bàsica que pugui efectuar operacions de suma, resta, multiplicació i divisió.
#El programa ha de demanar a l'usuari que ingressi dos números i després li preguntarà quina operació desitja realitzar.
#No pot dividir entre 0. Depenent de l'operació seleccionada, el programa farà el càlcul i mostrarà el resultat.
#Importo la biblioteca para crear el menu interactivo
while True:
    print("Calculator")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacio")
    print("4 - Divisio")
    print("5 - Sortir del programa del programa")
    opcion = input("\nSelecciona una opcio(un numero): ")
    if int(opcion) == 1:
        num1 = float(input("Introdueix el primer numero: "))
        num2 = float(input("Introdueix el segon numero: "))
        result_suma = num1 + num2
        print("%.2f" %result_suma)
        exit()
    elif int(opcion) == 2:
        num1 = float(input("Introdueix el primer numero: "))
        num2 = float(input("Introdueix el segon numero: "))
        result_resta = num1 - num2
        print("%.2f" %result_resta)
        exit()
    elif int(opcion) == 3:
        num1 = float(input("Introdueix el primer numero: "))
        num2 = float(input("Introdueix el segon numero: "))
        result_multiplicacion = num1 * num2
        print("%.2f" %result_multiplicacion)
        exit()
    elif int(opcion) == 4:
        num1 = float(input("Introdueix el primer numero: "))
        num2 = float(input("Introdueix el segon numero: "))
        result_dividsio = num1 * num2
        restant_divisio = num1 % num2
        print("%.2f" %result_dividsio)
        print("%.2f", "I si hi ha restant:" %restant_divisio)
        exit()
    elif int(opcion) == 5:
        print("Adeu")
        exit()
    else:
        print("Error 404. No es trova la operacio que vols fer torna seleccionrne una opcio correcta")