from math import sqrt
def czy_kwadrat(n):
    if (int(sqrt(n)))**2 == n:
        return 'TAK'
    else:
        return 'NIE'
n = int(input())
print(czy_kwadrat(n))