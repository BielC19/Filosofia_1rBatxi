#Fes un programa que donades dues mesures en reals d'una habitació (amplada i llargada), calculi quantes rajoles necessites enteres necessites comprar per fer l'habitació. Les rajoles mesuren 0,6m de costat i són quadrades.
amplada = float(input("Introdueix la amplada de l'habitacio en metres: "))
llargada = float(input("Introdueix la llargada de l'habitacio en metres: "))
mida_rejola = 0.6**2
area_habitacio = amplada*llargada
total_rejoles = area_habitacio/mida_rejola
print(f"A l'habitacio hi caven {total_rejoles}")
