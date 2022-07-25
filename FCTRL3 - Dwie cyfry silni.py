def cyfrysilni(n):
    if (n == 0 or n == 1):
        return '0 1'
    elif (n == 2):
        return  '0 2'
    elif(n == 3):
        return  '0 6'
    elif(n == 4):
        return '2 4'
    elif(n == 5 or n == 6 or n == 8):
        return '2 0'
    elif(n == 7):
        return '4 0'
    elif(n == 9):
        return '8 0'
    else:
        return '0 0'

def main():
    testy = int(input())
    for i in range(testy):
        n = int(input())
        print(cyfrysilni(n))

main()
