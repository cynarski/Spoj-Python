from math import floor,log


def przelicz(n,p):
    if n == 0:
        return 1
    else:
        return floor(log(n,10)/log(p,10)) + 1

testy = int(input())
for i in range(testy):
    n,p = [int(x) for x in input().split()]
    print(przelicz(n,p))