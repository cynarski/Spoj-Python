from collections import Counter

testy = int(input())
for _ in range(testy):
    n = int(input())
    tab = [int(x) for x in input().split()]
    tab = Counter(tab)
    x = list(tab.keys())
    y = list(tab.values())
    for i in range(len(x)):
        if int(y[i]) % 2 == 1:
            print(x[i])