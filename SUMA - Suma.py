import sys

try:
    suma = 0
    while True:
        x = int(input())
        if x != "":
            suma += x
            print(suma)

        else:
            break

except:
    sys.exit(0)
