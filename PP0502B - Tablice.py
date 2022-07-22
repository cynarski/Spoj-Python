testy = int(input())
for i in range(testy):
    liczby = list(map(int,input().split()))
    newlist = liczby[1:]
    newlist.reverse()
    print(*newlist)
