testy = int(input())
for i in range(testy):
    n = str(input())
    liczba = int(n,2)
    if liczba % 10 == 0:
        print('Tak')
    else:
        print('Nie')