import sys
try:
    suma1 = 0
    for line in sys.stdin:
        inputs = list(map(int,line.split()))
        suma = sum(inputs)
        suma1 += suma
        print(suma)
    print(suma1)

except:
    sys.exit(0)