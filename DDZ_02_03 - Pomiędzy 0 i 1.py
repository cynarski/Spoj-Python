dane = str(input())
zeros = []
ones = []
for i in range(len(dane)):
    if dane[i] == '1':
        ones.append(i)
    if dane[i] == '0':
        zeros.append(i)
a = int(zeros[0])
b = int(ones[-1])
result = str(dane[a+1:b])
if len(result) > 0:
    print(result)
else:
    print('PUSTY')