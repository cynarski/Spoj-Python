testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    people = int(dane[0]) -1
    sweets = int(dane[1])
    if people == 0:
        print("TAK")
    elif sweets%people != 0:
        print("TAK")
    elif sweets%people == 0:
        print("NIE")
