#Fes un programa que demani dues lletres minúscules i mostri les lletres de l'abecedari que hi ha entre elles, incloent-hi els extrems.

lletra_1 = input("Introdueix una lletra en minuscula: ")
lletra_2 = input("Introdueix una lletra en minuscula: ")

lletra_1 = ord(lletra_1)
lletra_2 = ord(lletra_2)

if lletra_1 in range(97, 122) and lletra_2 in range(97, 122) and lletra_1 <= lletra_2:
    print(f"Les letres que hi ha entre mitg son de '{chr(lletra_1)}' i '{chr(lletra_2)}' son: ")
    while (lletra_1 <= lletra_2):
        print(chr(lletra_1))
        lletra_1 += 1
else:
    print("No has introduit una lletra minuscula o  la prinmera es mes gran que la segona.")