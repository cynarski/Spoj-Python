n = int(input())
numbers = list(range(n+1))
result = []
if n == 0:
    print('0')
elif n == 1 or n == 2:
    print("NIE")
else:
    for i in range(1,len(numbers),2):
        result.append(numbers[i])
    for i in range(0,len(numbers),2):
        result.append(numbers[i])

    print(*result)
