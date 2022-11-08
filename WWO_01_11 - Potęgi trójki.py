import sys

lst = [3 ** i for i in range(19,-1,-1)]
def solution(n):
    counter = 0

    for i in lst:
        if n - i < 0:
            continue
        n -=i
        counter += 1

    return counter
try:
    lines = sys.stdin.read().split('\n')[1:]
    for line in lines:
        n = int(line)
        print(solution(n))
except:
    sys.exit(0)