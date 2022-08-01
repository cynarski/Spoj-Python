import sys

try:

    while True:
        dane = list(map(int,input().split()))
        counter = 0
        if dane != '':
            for i in range(2,len(dane)):
                if dane[i] == dane[0]:
                    counter += 1
        else:
            break
        print(counter)
        
except:
    sys.exit(0)
