import sys
from math import sqrt

try:

    x, y, r = [int(x) for x in input().split()]
    result = 0

    if sqrt(abs(y) * abs(y)) < r:
        result += 2
    elif sqrt(abs(y) * abs(y)) == r:
        result += 1

    if sqrt(abs(x) * abs(x)) < r:
        result += 2
    elif sqrt(abs(x) * abs(x)) == r:
        result += 1
    if sqrt(x**2 + y**2) == r:
        result -= 1

    print(result)
except:
    sys.exit(0)