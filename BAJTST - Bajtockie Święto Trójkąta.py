import math
from math import sqrt

def foo(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        p = (a+b+c)/2
        pole = sqrt((p*(p-a)*(p-b)*(p-c)))
        return pole
    else:
        return 0


t = int(input())
for _ in range(t):
    people,kreda = [x for x in input().split()]
    people = int(people)
    kreda = float(kreda)
    result = 0
    for i in range(people):
        a,b,c = [int(x) for x in input().split()]
        result += (foo(a,b,c)/10)* kreda
    result = round(result)
    print(result)
