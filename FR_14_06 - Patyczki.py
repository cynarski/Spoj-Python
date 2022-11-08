from collections import Counter
counter = 0
ilosc = int(input())
dane = list(map(int,input().split()))
lst = Counter(dane)
liczby = list(lst.values())
for i in range(len(liczby)):
    counter += int(liczby[i])//3
print(counter)