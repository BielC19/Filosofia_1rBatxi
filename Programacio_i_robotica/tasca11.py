#Fes un programa que converteixi un caràcter al seu valor enter d'ASCII. I després t'escrigui per pantalla: "Tu conversión esta hecha" "Señor X"
caracter_enter = input("Introdueix el caracter: ")              #l'usuari introdueix la lletra
caracter_ascii = ord(caracter_enter)                            #et converteix el caracter a ascii
print(f"La teva lletra '{caracter_enter}' a nombres ascii {caracter_ascii}")            #imprimeix el resultat