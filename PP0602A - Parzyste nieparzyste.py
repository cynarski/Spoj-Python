from typing import List

def lista(arr: List):
    result = []
    for i in range(len(arr)):
        if i % 2 == 1:
            result.append(arr[i])
    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(arr[i])

    return result

testy = int(input())
for i in range(testy):
    dane = list(map(int,input().split()))
    dane.pop(0)
    print(*lista(dane))
