def potenga(a,b):
    if(b==0):
        return '1'
    if(a%10 == 0):
        return '0'
    elif(a%10 == 1):
        return '1'
    elif(a%10 == 2):
        if(b%4 == 0):
            return '6'
        elif(b%4 == 1):
            return '2'
        elif(b%4 == 2):
            return '4'
        elif(b%4 == 3):
            return '8'
    elif(a%10 == 3):
        if(b%4 == 0):
            return '1'
        elif(b%4 == 1):
            return '3'
        elif(b%4 == 2):
            return '9'
        elif(b%4 == 3):
            return '7'
    elif(a%10 == 4):
        if(b%2 == 0):
            return '6'
        elif(b%2 == 1):
            return '4'
    elif(a%10 == 5):
        return '5'
    elif(a%10 == 6):
        return '6'
    elif(a%10 == 7):
        if(b%4==0):
            return '1'
        elif(b%4 == 1):
            return '7'
        elif(b%4 == 2):
            return '9'
        elif(b%4 == 3):
            return '3'
    elif(a%10 == 8):
        if(b%4 == 1):
            return '4'
        elif(b%4 == 2):
            return '2'
        elif(b%4 == 3):
            return '6'
        elif(b%4 == 0):
            return '8'
    elif(a%10 == 9):
        if(b%2 == 1):
            return '9'
        elif(b%2 == 0):
            return '1'



def main():
    testy=int(input())
    for i in range(testy):
        dane = (input('')).split(' ')
        a = int(dane[0])
        b = int(dane[1])
        wynik = potenga(a,b)
        print(wynik)
main()
