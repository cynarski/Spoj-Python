testy = int(input())
for i in range(testy):
    a,b= list(map(int,input().split()))
    result = []
    for j in range(a,b):
        if j % 2 == 0:
            result.append(j)
    if a in result:
        result.remove(a)
    if b in result:
        result.remove(b)
    if len(result) == 0:
        print("BRAK")
    print(*result)
