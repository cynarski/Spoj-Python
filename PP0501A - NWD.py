def nwd(a,b):
    if b > 0:
        return nwd(b,a % b)
    else:
        return a

testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    a = int(dane[0])
    b = int(dane[1])
    print(nwd(a,b))
