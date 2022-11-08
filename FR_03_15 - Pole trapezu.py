import sys
def pole(a,b):
    r = ((a*b)**0.5)/2
    return (a+b)*r
try:
    lines = sys.stdin.read().split('\n')[1:]
    for line in lines:
        a,b = [int(x) for x in line.split()]
        print('{:0.2f}'.format(pole(a,b)))

except:
    sys.exit(0)