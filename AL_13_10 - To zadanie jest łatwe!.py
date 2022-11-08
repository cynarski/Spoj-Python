import sys

def foo(a:str,b:str):

    pointer = 0
    for i in a:
        if i == b[pointer]:
            pointer += 1
            if pointer == len(b):
                return True

    return False

try:
    dane = sys.stdin.read().split('\n')[1:]
    for line in dane:
        a, b = [x for x in line.split()]
        if foo(a,b) == True:
            print("Tak")
        else:
            print("Nie")
except:
    sys.exit(0)