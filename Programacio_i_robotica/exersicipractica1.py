#Un negoci de sucs vol calcular el preu total de les begudes per als seus clients.
#El preu de cada suc és de 2.50 euros i el preu de cada batut és de 3.75 euros.
#El negoci també aplica un impost del 10% sobre el preu total de la comanda.
#Escriu un programa en Python que demani a l'usuari la quantitat de sucs i la quantitat de batuts que desitgen comprar.
#Després, el programa ha de calcular el cost total de la comanda (sense incloure l'impost) i després calcular l'impost del 10%.
#Finalment, el programa ha de mostrar el cost total de la comanda, incloent l'impost, amb un missatge clar i comprensible per al client.

preu_suc = 2.5
preu_batut = 3.75
impost = 0.1
cuantitat_sucs = int(input("Introdueix els productes que vols comprar separats per comes: "))
cuantitat_batuts = int(input("Introdueix els batuts que vols comprar separats per comes: "))

sense_impost = preu_suc*cuantitat_sucs + preu_batut*cuantitat_batuts
amb_impost = sense_impost + sense_impost*impost
print(f"Preu de la comanda sense impost es de {sense_impost}€\ni amb impostos seria {amb_impost}€")