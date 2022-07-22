def nww(a,b):
    if a < b:
        return nww(b,a)
    k = a
    while(k % b != 0):
        k += a
    return k

testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    print(nww(int(dane[0]),int(dane[1])))
