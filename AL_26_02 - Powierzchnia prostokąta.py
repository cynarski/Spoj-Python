testy = int(input())
for i in range(testy):
    n = int(input())
    if n % 2:
        print('BRAK')
    else:
        b = int(n/4)
        a = int(n/2 - b)
        area = a*b
        if area:
            print(int(area))
        else:
            print('BRAK')