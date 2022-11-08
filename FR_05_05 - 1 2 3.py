import sys
lst = [0] * 1000001
lst[2] = 4
lst[3] = 6
for j in range(4, 1000001):
    lst[j] = (lst[j - 2] * 2) % 101010101
try:
    lines = sys.stdin.read().split('\n')[1:]
    for line in lines:
        liczba = int(line)
        print(lst[liczba])
except:
    sys.exit(0)
