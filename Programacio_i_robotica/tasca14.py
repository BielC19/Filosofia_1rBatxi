#Primer estimar i després comprovar el resultat
a = 1
b = 3
c = 'a'
d = 'd'
x = 0.0
y = 1.2
s1 = "aab"
s2 = "ccd"

a > 1 and b < 2,                #False
c == '7' and d == 'd',          #False
c != 'a' and c != 'd',          #False
a == 1 and b == 3,              #True
s1 > "aaa" and s1 < "zzz",      #True
s1 != 52 and s1 == "aab",       #True
a // b == 0 and a % b == d      #Flase


print(a > 1 and b < 2, "\n",
c == '7' and d == 'd', "\n",
c != 'a' and c != 'd', "\n",
a == 1 and b == 3, "\n",
s1 > "aaa" and s1 < "zzz", "\n",
s1 != 52 and s1 == "aab", "\n",
a // b == 0 and a % b == d)