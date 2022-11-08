import sys

try:
    dane = sys.stdin.read().split('\n')[1:]
    for line in dane:
        n = int(line)
        print(n*(n+1)*(2*n+1)//6)

except:
    sys.exit(0)