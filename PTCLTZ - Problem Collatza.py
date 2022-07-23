def Collatz(s,n):
    if s == 1:
        return n
    elif s == 0:
        return 0
    if s % 2 == 1:
        return Collatz(3*s + 1, n = n+1)
    else:
        return Collatz(s/2, n = n+1)

testy = int(input())
result = 0
for i in range(testy):
    print(Collatz(int(input()),result))


