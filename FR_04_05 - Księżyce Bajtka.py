testy = int(input())
for i in range(testy):
    a, b = list(map(float, input().split()))
    print('{:0.2f}'.format(2*a*b)) 