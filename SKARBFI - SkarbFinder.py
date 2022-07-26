testy = int(input())
for i in range(testy):
    clues = int(input())
    ver = 0
    hor = 0
    for i in range(clues):
        dane = list(map(int,input().split()))
        if dane[0] == 0:
            ver += dane[1]
        elif dane[0] == 1:
            ver -= dane[1]
        elif dane[0] == 2:
            hor += dane[1]
        elif dane[0] == 3:
            hor -= dane[1]

    if ver == 0 and hor == 0:
        print('studnia')
    elif ver > 0:
        print('0',ver)
    elif ver < 0:
        print('1', abs(ver))
    if hor > 0:
        print('2', hor)
    elif hor < 0:
        print('3',abs(hor))
