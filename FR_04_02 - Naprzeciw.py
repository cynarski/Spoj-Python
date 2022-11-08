import sys

def stol(n:int,k:int):
    if n % 2:
        return 'BRAK'
    else:
        return  int(k - n/2) if k > n/2 else int(k + n/2)
try:
    lines = sys.stdin.read().split('\n')[1:]
    for line in lines:
        dane = line.split()
        print(stol(int(dane[0]),int(dane[1])))
except:
    sys.exit(0)
