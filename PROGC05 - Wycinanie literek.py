import sys
try:
    while True:
        dane = list(map(str,input().split()))
        result = ''
        for i in dane[1]:
            if i != dane[0]:
                result += i
        print(result)

except:
    sys.exit(0)