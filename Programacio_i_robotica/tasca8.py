#Fes un programa que  et donada una quantitat d'ous calculi quantes capses es poden omplir amb aquests ous i et digui els sobrants (cada capsa 6 ous).
ous = int(input("Ingrese la cantidad de huevos:"))

caixes_plenes = ous // 6
ous_sobrants = ous % 6
if (ous_sobrants>0):
  caixes_plenes += 1
print(f"Se pueden llenar {caixes_plenes} cajas de huevos.")
print(f"Sobran {ous_sobrants} huevos.")