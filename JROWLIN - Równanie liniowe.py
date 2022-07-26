import sys

def rownanie(a,b,c):
    if(a == 0 and b == c):
        print('NWR')
    elif(a == 0 and b != c):
        print('BR')
    else:
        print('{:.2f}'.format(round((c-b)/a,2)))

try:
    dane = list(map(float,input().split()))
    rownanie(dane[0], dane[1],dane[2])

except:
    sys.exit(0)

