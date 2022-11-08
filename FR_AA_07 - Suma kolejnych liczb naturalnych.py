n,s = [int(x) for x in input().split()]
a = int((2*s - n*(n-1))/(2*n))
liczby = [a + i for i in range(n)]
print(*liczby)