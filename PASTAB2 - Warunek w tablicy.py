n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

chr = input().split(' ')
if chr[0] == '<':
    for i in range(n):
        if lst[i] < int(chr[1]):
            print(lst[i])
elif chr[0] == '>':
    for i in range(n):
        if lst[i] > int(chr[1]):
            print(lst[i])