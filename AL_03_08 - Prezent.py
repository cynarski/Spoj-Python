dane = [int(x) for x in input().split()]

max = max(dane)
maxDruga = 0
for i in range(len(dane)):
    if dane[i] == max:
        dane[i] = 0

    if dane[i] > maxDruga:
        maxDruga = dane[i]

if maxDruga == 0:
    print(max)
else:
    print(maxDruga)