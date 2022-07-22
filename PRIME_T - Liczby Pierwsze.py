import math

def czypierwsza(n):
    if n == 2:
        return 'TAK'
    if n % 2 == 0 or n == 1:
        return 'NIE'
    pierwiastek =  int(n ** 0.5) + 1
    for i in range(3,pierwiastek,2):
        if n % i == 0:
            return 'NIE'
    return 'TAK'


testy = int(input())
for i in range(testy):
    liczba = int(input())
    print(czypierwsza(liczba))
