#Fes-me un programa que donades les tres longituds en cm d'un triangle (3 inputs) determini quin tipus de triangle és (escalè, isòsceles o ).
a = input("Instrodueix una de les mides en cm: ")
b = input("Instrodueix una de les mides en cm: ")
c = input("Instrodueix una de les mides en cm: ")

if a==b and a==c and b==c:
    print("el triangles es equilàter:)")
elif a>b and a>c:
    print("el triangle es escalè:)")
elif a<b and a<c:
    print("el triangle es isòsceles:)")
else:
    print("has introduit les dades malament")