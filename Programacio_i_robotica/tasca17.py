#Fes un programa que et digui si uns valors donats per l'usuari d'x i y estan dintre de la zona marcada en vermell.

x = float(input("Introdueix la coordenada x: "))
y = float(input("Introdueix la coordenada y: "))


comprovacio_1 = x <= 1 and x >= 0 and y <= 1 and y >= 0
comprovacio_2 = y <= 2 and y >= 0 and x >= 2 and x <= 3
cocmprovacioTot = comprovacio_1 or comprovacio_2
print(f"\nEl primer quadrat es '{comprovacio_1}' dints del quadrat.")
print(f"El segon quadrat es '{comprovacio_2}' dints del quadrat.")

print(f"\nLes cortenades totals son '{cocmprovacioTot}' dints del quadrat.\n")