n = int(input())
lst = list(map(int,input().split()))
i = 0
result = 0
while i < len(lst)-2:
    if lst[i] + lst[i+1] == lst[i+2]:
        result += 1
    i += 1
print(result)
