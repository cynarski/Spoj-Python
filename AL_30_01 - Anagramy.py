dane = input().split(' ')
wyraz = str(dane[0])
testy = int(dane[1])
wyraz = list(wyraz)
wyraz.sort()
licznik = 0
for i in range(testy):
    word = str(input())
    word = list(word)
    word.sort()
    if word == wyraz:
        licznik += 1
print(licznik)