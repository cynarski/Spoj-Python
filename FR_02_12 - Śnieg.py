import sys

def nwd(a,b):
    if b > 0:
        return nwd(b,a % b)
    else:
        return a

def nww(a,b):
    return (a*b)/nwd(a, b)


lines = sys.stdin.read().split('\n')
for line in lines:
    k1,k2,k3,m = [int(x) for x in line.split()]
    wynik = nww(nww(k1,k2),k3)
    wynik = 100*m/wynik
    print(int(wynik))

