import sys
try:
    while True:
        word = input()
        print(word[::-1])

except:
    sys.exit(0)