a = int(input())
aset = list(map(int,input().split()))
b = int(input())
bset = list(map(int,input().split()))
suma = []
iloczyn = []
for i in range(len(aset)):
    suma.append(aset[i])
for i in range(len(bset)):
    if bset[i] in suma:
        suma.remove(bset[i])
suma += bset
for i in range(len(aset)):
    if aset[i] in bset:
        iloczyn.append(aset[i])
suma.sort()
print(*suma)
iloczyn.sort()
if len(iloczyn) == 0:
    print("NULL")
else:
    print(*iloczyn)