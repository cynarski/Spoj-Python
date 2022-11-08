from math import factorial
dane = [factorial(i) for i in range(13)]
a,b = [int(x) for x in input().split()]
result = 0
for i in dane:
   if a <= i <= b:
       result += 1
print(result)