testy = int(input())
for i in range(testy):
    n = list(map(float, input().split()))
    n.pop(0)
    average = sum(n)/len(n)
    x = abs(average - n[0])
    closest = x
    number = n[0]
    for j in n:
        x = abs(average - j)
        if x < closest:
            closest = x
            number = j
    print(int(number))
