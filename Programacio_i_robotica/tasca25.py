#Haz un programa que recorra los números del 1 al 100 y los escriba por pantalla separados por comas. 
#Algunos números se deben sustituir por una palabra, según los casos siguientes:
#En los divisibles por 3, hay que escribir "Fizz".
#En los divisibles por 5, hay que escribir "Buzz".
#En los divisibles por 3 y 5, hay que escribir "FizzBuzz".
i = 0
while i<=100:
    if i==100:
        print("Buzz", end="")
    elif (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz,", end=" ")
    elif i % 3 == 0:
        print("Fizz,", end=" ")
    elif i % 5 == 0:
        print("Buzz,", end = " ")
    else:
        print(i, end =", ")
    i += 1
print("\n\n")
i = 0
a = []
while i<=100:
    if i==100:
        print("Buzz", end="")
    elif (i % 3 == 0) and (i % 5 == 0):
        a.append("FizzBuzz")
    elif i % 3 == 0:
        a.append("Fizz")
    elif i % 5 == 0:
        a.append("Buzz")
    else:
        a.append(i)
    i += 1

print(a)
