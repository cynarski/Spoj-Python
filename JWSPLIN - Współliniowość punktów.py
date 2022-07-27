def czy_wspolniniowe(xa,ya,xb,yb,xc,yc):
    if xb - xa == 0:
        aAB = 0
    else:
        aAB = (yb - ya)/(xb - xa)
    if xc - xb == 0:
        aBC = 0
    else:
        aBC = (yc - yb) / (xc - xb)
    if aAB == aBC:
        print('TAK')
    else:
        print('NIE')



testy = int(input())
for i in range(testy):
    dane = list(map(int,input().split()))
    czy_wspolniniowe(dane[0],dane[1],dane[2],dane[3],dane[4],dane[5])
