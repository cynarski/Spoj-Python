from math import sqrt


testy = int(input())
for _ in range(testy):
    x = int(input())
    print('{:0.2f}'.format((sqrt(2)*x**3)/12))