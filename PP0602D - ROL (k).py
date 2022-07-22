def rol(tab,przesuniecie):
    newtab1 = tab[przesuniecie:]
    newtab2 = tab[:przesuniecie]
    return newtab1 + newtab2

dane = input().split(' ')
ilosc = int(dane[0])
przesuniecie = int(dane[1])
tablica = list(map(int,input().split()))
print(*rol(tablica,przesuniecie))
