testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    n = int(dane[0])
    m = int(dane[1])
    cakes = 0
    for j in range(n):
        time = int(input())
        cakes += int(24 * 3600/time)
    if cakes % m != 0:
        print(int(cakes/m) + 1)
    else:
        print(int(cakes/m))


