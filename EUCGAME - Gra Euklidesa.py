testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    a = int(dane[0])
    b = int(dane[1])
    while a != b:
        tmp = a
        a -= b
        if (a < 0):
            b = -a
            a = tmp
    print(a+b)


