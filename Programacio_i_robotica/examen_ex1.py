#Es vol realitzar un programa que et calculi el nombre enter de galledes d’aigua per omplir
#una piscina rodona d’uns determinats litres. Per això el programa haurà de fer el següent:
#1- Saludar a l’usuari.
#2- Preguntar a l’usuari el diàmetre i altura (floats) de la piscina i guardar cada valor a una variable.
#3- Calcular la quantitat de litres enters de la piscina Mostrar-ho a l’usuari. (1L= 1dm3).
#4- Calcular el nombre enter de galledes necessàries per omplir la piscina i els litres sobrants
#que no poden omplir-se amb una galleda plena. (1 galleda = 8L ). Mostrar-ho a l’usuari.
#5- Si cada hora l’usuari pot omplir 60 galledes calcular el nombre enter d’hores per omplir la
#piscina i els minuts restants. Mostra-ho a l’usuari.
#6- Acomiadar-se de l’usuari.

#1
nom_usuari = input("Com et dius?")          #demana el nom a l'usuari
print(f"Hola {nom_usuari}\n\n")             #saluda a l'usuari
#2
diametre_picina = float(input("Introdueix el diametèr en m de la teva picina: "))   #demana el diametre
altura_picina = float(input("Introdueix el altura en m de la teva picina: "))       #demana l'altura
#3
import math                     #importes la llibraria math per poder agafer el numero pi
numero_pi = math.pi             #pose el numero pi a una variable

diametre_picina_dm = diametre_picina * 10   #passes el diametre a dm
altura_picina_dm = altura_picina * 10       #passes l'altura a dm

calculacio_volum = numero_pi * (diametre_picina_dm/2)**2 * altura_picina_dm     #calculas el volum de la picina

print(f"\n\nA la picina i caven {calculacio_volum}l")                       #imprimeix els litres que hio caven a la picina
#4
mida_galleda = 8
numero_galledes = calculacio_volum//8                       #convereteix de litres a galledes
print(f"\nNecesites {numero_galledes} galledes i et falten {calculacio_volum%8} lites per omplira la teva picina de {calculacio_volum} litres")         #torna les galles, els litres sobrants i els dtotals de la picina
#5
galledes_hora = numero_galledes//60                 #passa de galledes a hores
galledes_hora_sobrants = numero_galledes%60         #minuts sobrants
min_restant = galledes_hora_sobrants                #minuts sobrants
print(f"\nCalcen {galledes_hora} hores i {min_restant} minuts per omplir la")       #torna el numero de hores que trigues a omplir la picina i els minuts restants
#6
print(f"\nFins aviat {nom_usuari}.")