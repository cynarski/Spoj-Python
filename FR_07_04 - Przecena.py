testy = int(input())
for i in range(testy):
    a,b = list(map(int,input().split()))
    z = 100 - a
    q = z * (1-(b*0.01))
    result = 100 -q
    print('{:0.2f}'.format(result))