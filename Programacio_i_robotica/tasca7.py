#Donat un temps en segons calcula els minuts que són i els segons restants
segons = float(input('Quants segon vols comvertir? '))
minuts = segons//60
segons_restans = segons%60
print(f"{segons}s son {minuts}min i {segons_restans}s.")