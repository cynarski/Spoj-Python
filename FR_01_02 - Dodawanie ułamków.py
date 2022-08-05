from math import gcd
def nww(a,b):
    if a < b:
        return nww(b,a)
    k = a
    while(k % b != 0):
        k += a
    return k
u1,u2 = list(map(str,input().split()))
liczniku1 = liczniku2 = mianowniku1 = mianowniku2=""
ulamek1 = ''
ulamek2 = ''
for i in range(len(u1)):
    ulamek1 += u1[i]
for i in range(len(u2)):
    ulamek2 += u2[i]
for i in range(len(u1)):
    if u1[i] == '/':
        liczniku1 = u1[:i]
        mianowniku1 = u1[i+1:]
for i in range(len(u2)):
    if u2[i] == '/':
        liczniku2 = u2[:i]
        mianowniku2 = u2[i+1:]
mianownik = int(mianowniku1) * int(mianowniku2)
licznik = int((mianownik/int(mianowniku1)) * int(liczniku1) + (mianownik/int(mianowniku2)) * int(liczniku2))
ulamek3 = ''
if gcd(licznik,mianownik) == 1:
    ulamek3 = str(licznik) + '/' + str(mianownik)
    print(ulamek1, '+', ulamek2, '=', ulamek3)
elif gcd(licznik,mianownik) != 1:
    licznik1 = int(licznik / gcd(licznik, mianownik))
    mianownik1 = int(mianownik / gcd(licznik, mianownik))
    ulamek3 = str(licznik1) + '/' + str(mianownik1)
    print(ulamek1, '+', ulamek2, '=', ulamek3)