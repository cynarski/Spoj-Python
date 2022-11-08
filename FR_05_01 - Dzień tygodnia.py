testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    liczba = int(dane[1])
    if str(dane[0]) == 'Pn':
        if liczba % 7 == 1:
            print('Wt')
        elif liczba % 7 == 2:
            print('Sr')
        elif liczba % 7 == 3:
            print('Cz')
        elif liczba % 7 == 4:
            print('Pt')
        elif liczba % 7 == 5:
            print('So')
        elif liczba % 7 == 6:
            print('Nd')
        elif liczba % 7 == 0:
            print('Pn')
    elif str(dane[0]) == 'Wt':
        if liczba % 7 == 0:
            print('Wt')
        elif liczba % 7 == 1:
            print('Sr')
        elif liczba % 7 == 2:
            print('Cz')
        elif liczba % 7 == 3:
            print('Pt')
        elif liczba % 7 == 4:
            print('So')
        elif liczba % 7 == 5:
            print('Nd')
        elif liczba % 7 == 6:
            print('Pn')
    elif str(dane[0]) == 'Sr':
        if liczba % 7 == 6:
            print('Wt')
        elif liczba % 7 == 0:
            print('Sr')
        elif liczba % 7 == 1:
            print('Cz')
        elif liczba % 7 == 2:
            print('Pt')
        elif liczba % 7 == 3:
            print('So')
        elif liczba % 7 == 4:
            print('Nd')
        elif liczba % 7 == 5:
            print('Pn')
    elif str(dane[0]) == 'Cz':
        if liczba % 7 == 5:
            print('Wt')
        elif liczba % 7 == 6:
            print('Sr')
        elif liczba % 7 == 0:
            print('Cz')
        elif liczba % 7 == 1:
            print('Pt')
        elif liczba % 7 == 2:
            print('So')
        elif liczba % 7 == 3:
            print('Nd')
        elif liczba % 7 == 4:
            print('Pn')
    elif str(dane[0]) == 'Pt':
        if liczba % 7 == 4:
            print('Wt')
        elif liczba % 7 == 5:
            print('Sr')
        elif liczba % 7 == 6:
            print('Cz')
        elif liczba % 7 == 0:
            print('Pt')
        elif liczba % 7 == 1:
            print('So')
        elif liczba % 7 == 2:
            print('Nd')
        elif liczba % 7 == 3:
            print('Pn')
    elif str(dane[0]) == 'So':
        if liczba % 7 == 3:
            print('Wt')
        elif liczba % 7 == 4:
            print('Sr')
        elif liczba % 7 == 5:
            print('Cz')
        elif liczba % 7 == 6:
            print('Pt')
        elif liczba % 7 == 0:
            print('So')
        elif liczba % 7 == 1:
            print('Nd')
        elif liczba % 7 == 2:
            print('Pn')
    elif str(dane[0]) == 'Nd':
        if liczba % 7 == 2:
            print('Wt')
        elif liczba % 7 == 3:
            print('Sr')
        elif liczba % 7 == 4:
            print('Cz')
        elif liczba % 7 == 5:
            print('Pt')
        elif liczba % 7 == 6:
            print('So')
        elif liczba % 7 == 0:
            print('Nd')
        elif liczba % 7 == 1:
            print('Pn')