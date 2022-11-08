import sys
try:
    while True:
        n = int(input())
        liczba = str(bin(n)[2:])
        liczba2 = liczba[::-1]
        print(int(liczba2,2))
except:
    sys.exit(0)