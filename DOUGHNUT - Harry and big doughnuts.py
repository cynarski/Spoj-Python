testy = int(input())
for i in range(testy):
    c,k,w = map(int,input().split())
    if c*w > k:
        print('no')
    else:
        print('yes')