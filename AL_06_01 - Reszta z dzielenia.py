testy = int(input())
for i in range(testy):
    a,b = list(map(int,input().split()))
    reszta = a%b
    if reszta < 0 and b > 0:
        reszta +=b
    elif reszta < 0 and b < 0:
        reszta -= b
    print(reszta)
