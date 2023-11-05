#Feu un exercici que donat un número en format ABCD, extregui els nombres A, B,C i D i trobi el nombre corresponent a la taula ASCII +23.
lletres = "ABCD"
lletra_a_lletra = []
lletres_sum = []
for lletra in lletres:
    lletra_a_lletra.append(lletra)
for i in lletra_a_lletra:
    lletres_sum.append(chr(ord(lletra_a_lletra) + 23))
    
