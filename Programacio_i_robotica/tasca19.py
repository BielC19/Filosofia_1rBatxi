#Fes el mateix que la Tasca 17, però el programa haurà de dir si es troba fora de la zona vermella 
#(1 si es troba fora, 0 si es troba dintre). Utilitza l'operador NOT.

x = float(input("Introdueix la coordenada x: "))
y = float(input("Introdueix la coordenada y: "))


comprovacio_1 = x <= 1 and x >= 0 and y <= 1 and y >= 0
comprovacio_2 = y <= 2 and y >= 0 and x >= 2 and x <= 3
cocmprovacioTot = comprovacio_1 or comprovacio_2
print(f"\nEl primer quadrat es '{not comprovacio_1}' dints del quadrat.")
print(f"El segon quadrat es '{not comprovacio_2}' dints del quadrat.")

print(f"\nLes cortenades totals son '{not cocmprovacioTot}' dints del quadrat.\n")