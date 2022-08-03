inputs = list(map(int,input().split()))
a = inputs[0]
b = inputs[1]
c = inputs[2]
if a < b <= c or a < c <= b:
    print("TAK",1)
elif b < a <= c or b < c <= a:
    print("TAK",2)
elif c < b <= a or c < a <= b:
    print("TAK",3)
else:
    print("NIE")