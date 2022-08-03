import math
x,y,r = list(map(int,input().split()))
testy = int(input())
for i in range(testy):
    a,b = list(map(int,input().split()))
    if math.sqrt((x-a)**2 + (y-b)**2) == r:
        print('E')
    elif math.sqrt((x-a)**2 + (y-b)**2) <= r:
        print('I')
    else:
        print('O')