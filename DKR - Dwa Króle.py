def dwa_krole(n,m):
    return (n*m -9)*(m-2)*(n-2) + 4*(n*m -4) + (n*m -6)*(2*(m-2) + 2*(n-2))

testy = int(input())
for _ in range(testy):
    n,m = [int(x) for x in input().split()]
    print(dwa_krole(n,m))