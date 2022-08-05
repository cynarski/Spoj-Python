while True:
    x = int(input())
    if x == 0:
        break
    elif x % 15 == 0:
        print("TAK")
    else:
        print("NIE")