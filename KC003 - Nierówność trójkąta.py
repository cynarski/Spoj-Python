import sys
def czy_trojkat(a,b,c):
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        print('1')
    else:
        print('0')
try:
    while True:
        inputs = list(map(float,input().split()))
        czy_trojkat(inputs[0],inputs[1],inputs[2])
except:
    sys.exit(0)