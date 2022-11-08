def manhatan(arr:list,lst:list):
    result = 0
    for i in range(len(arr)):
        if arr[i] != lst[i]:
            result += abs(int(arr[i]) - int(lst[i]))
    return result

k,n = list(map(int,input().split()))
for i in range(n):
    z = list(map(int,input().split()))
    do = list(map(int,input().split()))
    print(manhatan(z,do))
