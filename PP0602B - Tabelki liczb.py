testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    row = int(dane[0])
    col = int(dane[1])
    result = []
    for i in range(row):
        result.append(list(map(int,input().split())))

    for i in range(row):
        for j in range(col):
            if i == 0: # pierwszy wiersz
                if j == col-1:
                    print(result[i+1][j],end =' ')
                else:
                    print(result[i][j+1], end=' ')
            elif i == row-1: # drugi wiersz
                if j == 0:
                    print(result[i-1][j],end = ' ')
                else:
                    print(result[i][j-1],end=' ')
            else:
                if j == 0:
                    print(result[i-1][j],end=' ')
                elif j == col-1:
                    print(result[i+1][j],end=' ')
                else:
                    print(result[i][j],end=' ')
        print()
