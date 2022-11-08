import sys
def pole(p1:int,p2:int):
    return p1 + 2 * p2 + ((p2/p1)**2)*p1
try:
    lines = sys.stdin.read().split('\n')
    for line in lines:
        p1,p2 = [int(x) for x in line.split()]
        print('{:0.2f}'.format(pole(p1,p2)))
except:
    sys.exit(0)