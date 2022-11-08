def matrix(row: int,col: int):
    result = []
    for i in range(row):
        result.append(list(map(int,input().split())))
    for i in range(col):
        for j in range(row):
            print(int(result[j][i]), end= ' ')

        print()

dane = input().split(' ')
row = int(dane[0])
col = int(dane[1])
matrix(row,col)
