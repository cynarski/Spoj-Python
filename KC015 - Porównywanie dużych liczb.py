import sys
try:
    while True:
        dane = list(map(str,input().split()))
        if dane[1] == '==':
            if int(dane[0]) == int(dane[2]):
                print('1')
            else:
                print('0')
        elif dane[1] == '<=':
            if int(dane[0]) <= int(dane[2]):
                print('1')
            else:
                print('0')

        elif dane[1] == '>=':
            if int(dane[0]) >= int(dane[2]):
                print('1')
            else:
                print('0')
        elif dane[1] == '!=':
            if int(dane[0]) != int(dane[2]):
                print('1')
            else:
                print('0')
except:
    sys.exit(0)