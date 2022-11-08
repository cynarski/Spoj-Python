import sys

try:
    while True:
        dane = list(map(str,input().split()))
        if dane != '':
            if (dane[0] == '+'):
                print(int(dane[1]) + int(dane[2]))
            elif(dane[0] == '-'):
                print(int(dane[1]) - int(dane[2]))
            elif(dane[0] == '*'):
                print(int(dane[1]) * int(dane[2]))
            elif(dane[0] == '/'):
                print(int(int(dane[1]) / int(dane[2])))
            elif(dane[0] == '%'):
                print(int(dane[1]) % int(dane[2]))
            else:
                break
except:
    sys.exit(0)
