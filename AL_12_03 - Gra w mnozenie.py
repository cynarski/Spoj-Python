
import sys
import fileinput
try:
    with fileinput.input() as f:
        for n in f:
            n = int(n)
            if n <= 9:
                print('A')
            while n > 9:
                n /= 18
            print('B' if n <= 1 else "A")


except:
    sys.exit(0)