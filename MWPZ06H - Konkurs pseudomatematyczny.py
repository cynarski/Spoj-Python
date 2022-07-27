testy = int(input())
for i in range(testy):
    result = []
    ilosc = int(input())
    dane = list(map(int,input().split()))
    d_max = max(dane)
    for j in range(len(dane)):
        if dane[j] == d_max:
            result.append(dane[j])

    for j in range(dane.count(d_max)):
        dane.remove(d_max)

    dane.sort()
    result += dane
    print(*result)
