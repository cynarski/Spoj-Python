suma = 0
for i in range(4):
    inputs = list(map(int,input().split()))
    suma += inputs[0] - inputs[1]

print(suma)