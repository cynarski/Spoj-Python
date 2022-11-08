def newton(n,k):
    if n < 0 or k < 0:
        return  None
    if n == 0 and k == 0:
        return 1
    result = 1
    for i in range(1,k + 1):
        result = result * (n - i + 1)/i
    return result

testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    n = int(dane[0])
    k = int(dane[1])
    print(round(newton(n,k)))