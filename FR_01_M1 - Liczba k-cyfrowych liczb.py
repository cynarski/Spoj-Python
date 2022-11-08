import sys


lines = sys.stdin.read().strip().split('\n')[1:]
for line in lines:
    k,n = [int(x) for x in line.split()]
    if k == 1:
        print(n)
    else:
        print(n**(k-1) * (n-1))