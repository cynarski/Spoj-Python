def rol(tab):
    newtab1 = tab[1:]
    newtab1.append(tab[0])
    return newtab1

testy = int(input())
for i in range(testy):
    dane = list(map(int,input().split()))
    print(*rol(dane[1:]))
