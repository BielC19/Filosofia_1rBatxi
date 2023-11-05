#Fes un programa que donada una entrada en format HH:MM:SS
#tu mAadre tiene una polla que ya la quisierta yo me dio pena por tu opadreEt retorni el mateix número a la sortida sumant 1 segon.
HH = int(input("indtroueix la hora en format HH: "))
MM = int(input("Introdueix els minuts en format MM: "))
SS = int(input("Introdueix els segons en format SS: "))


if HH==24 and MM==60 and SS==60:
    HH = 00
    MM = 00
    SS = 00
elif HH>=24 and MM>=60 and SS>=60:
    HH = 24-HH
    MM = MM-60
    SS = SS-60

print(f"La hora es {HH}:{MM}:{SS}")
