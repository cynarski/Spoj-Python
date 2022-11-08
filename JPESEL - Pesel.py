from typing import List
def pesel(arr: List):
    for i in range(len(arr)):
        if i == 1 or i == 5 or i == 9:
            arr[i] *= 3
        elif i == 2 or i == 6:
            arr[i] *= 7
        elif i == 3 or i == 7:
            arr[i] *= 9
    if sum(arr) % 10 == 0:
        print('D')
    else:
        print('N')

testy = int(input())
for i in range(testy):
    pesell = str(input())
    dane = []
    for j in pesell:
        dane.append(int(j)) # zamiana stringa na inta - liste
    pesel(dane)