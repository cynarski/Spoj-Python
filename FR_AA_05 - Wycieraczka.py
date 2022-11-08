from math import sqrt


a, r = [int(x) for x in input().split()]
n = int(input())
result = 0
for i in range(n):
    x, y = [int(x) for x in input().split()]
    if sqrt((a-x)**2 + y**2) > r:
        result += 1
print(result)