import sys
from math import gcd
import fileinput

def FingLCM(a, b):
    return a * b // gcd(a, b)


def rangeDevisor(m, n, a, b):
    # Find LCM of a and b
    lcm = FingLCM(a, b)

    a_divisor = n // a - (m - 1) // a
    b_divisor = n // b - (m - 1) // b

    # Find common divisor by using LCM
    common_divisor = n // lcm - (m - 1) // lcm

    ans = a_divisor + b_divisor - common_divisor
    return ans
try:
    a,b = [int(x) for x in input().split()]
    while True:
        c,d = [int(x) for x in input().split()]
        print(rangeDevisor(c,d,a,b))

except:
    sys.exit(0)