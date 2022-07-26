testy = int(input())
for i in range(testy):
    dane = str(input())
    result = ""
    if len(dane) % 2 == 0:
        print(dane[:int(len(dane)/2)]) # wypisywanie wyrazu do wyznaczonego miejsca
