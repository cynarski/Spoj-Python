import sys

try:
    one, two, three = map(int, input().split())
    names = []
    girls = boys = 0

    for c in range(3):
        names.extend(input().split())

    for name in names:
        if name[-1] == 'a':
            girls += 1
        else:
            boys += 1

    if boys < girls:
        print(boys)
    else:
        print(girls)
except:
    sys.exit(0)
