lst = []
testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    if int(dane[0]) in lst:
        continue
    else:
        lst.append(int(dane[0]))
print(len(lst))