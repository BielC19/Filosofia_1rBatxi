#Fes un programa que donada un nombre per l'usuari et digui si NO és par.
#Si NO és par (ha de sortir un 1 per pantalla, si és par un 0).
#Has d'utilitzar l'operador NOT.

numero_introduit = int(input("Introdueix un nombre: "))

b = numero_introduit % 2 == 0
print(b)