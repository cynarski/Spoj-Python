x,y = list(map(int,input().split()))
result = ''
for i in range(x,y+1):
    if i % 6 == 0:
        result+='ab'
    elif i % 2 == 0 and i % 3 != 0:
        result +='a'
    elif i % 3 == 0 and i % 2 != 0:
        result +='b'
print(result)