n,r = list(map(int,input().split()))
n = 2*n
n = n + 5
n = n*50
n += 1771
x = n - r
print(int(x%100))