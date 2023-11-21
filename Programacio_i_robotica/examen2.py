# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
while True:
    print("Hello world") 
    print("Introdueix 10 nombres \n")
    nums = []

    for i in range(3):              #aqui hi ha el bucle per els 10 inputs
        a = int(input("introdueix un nombre:"))         #el input
        while a < 0:                                    #el comprovador de que es mes gran de 0
            a = int(input("introdueix un valor mes gran que 0: "))
        nums.append(a)

    q = int(input("si vols calcular el factorial prem 1, si vols calcular el qualdrat dels nombres senars prem 2, per sortir del progrma  prem 0:  "))      #input per saber que ha de fer l'examen
    
    for n in nums:      #primer bucle que
        
        if n%2 != 0:    #comprovador de seners
            if q == 1:      #comprova que has triat i fa el factorial
                b = 1       #variable auxiliar
                for m in range(n):
                    b += m*b
                print(f"El teu resultat: {b}")
            elif q == 2:        #comprova el que has triat i fa el quadrat
                print("el quadrat es:",n**2)
            elif q == 0:        #comprova i et treu del programa
                print("Adeu")
                exit()
            else:           #per si fas algo malament
                print("error el compilador a chuparla perque ets burru i no has posat cap dels numeros q tocava \n :)")
        elif n%2 == 0:      #comprovador de parells
            print(f"Numeros parells: {n}")
        elif n == 0:
            print ("aquest numero es 0")
        else:               #per si fas algo malament
            print("error el compilador a chuparla \n :)")
    z = int(input("vols repetirho? si es que si posa 1 i si es quie no posa 0: "))
    if z == 0:
        exit()
