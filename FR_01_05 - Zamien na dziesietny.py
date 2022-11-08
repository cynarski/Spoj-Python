import sys
try:
    lines = sys.stdin.read().split('\n')[1:]
    for line in lines:
        n, liczba = [x for x in line.split()]
        print(int(liczba, int(n)) % 1010101)
except:
    sys.exit(0)