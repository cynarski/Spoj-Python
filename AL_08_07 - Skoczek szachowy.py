testy = int(input())
for i in range(testy):
    n = int(input())
    if n == 1:
        print(8)
    elif n == 2:
        print(33)
    else:
        suma = 0
        x = int(n/2)
        suma += 4 * n * n + 3 * n + 1
        if n % 2 == 0 :
            suma += 2 * n * n + n
        else:
            suma += 2 * ((x + 1) * (2 * n + 1) - n)
        suma += 4 * (n - x) * x
        print(suma)