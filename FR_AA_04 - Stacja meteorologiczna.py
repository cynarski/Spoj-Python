n = input()
lst = list(map(int,input().split()))
result = []
for i in lst:
    if i not in result:
        result.append(i)
print(len(result))