#Fes un programa que llegeixi 2 números reals que són les coordenades x i d'un punt del pla 2D.
#El programa ha d'escriure  1 (dins) o 0(fora) segons si el punt es troba dins o fora del quadrat següent.

x = float(input("Introdueix la primera coordenada: "))
y = float(input("Introdueix la segona coordenada: "))

quadrat = 1

comprovacio_X = x <= quadrat and x >= 0
comprovacio_Y = y <= quadrat and y >= 0
cocmprovacioTot = comprovacio_X and comprovacio_Y
print(f"\nLa cortenada x es '{comprovacio_X}' dints del quadrat.")
print(f"La cortenada y es '{comprovacio_Y}' dints del quadrat.")

print(f"\nLes cortenades totals son '{cocmprovacioTot}' dints del quadrat.\n")