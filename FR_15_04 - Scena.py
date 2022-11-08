a, b = [int(x) for x in input().split()]
if a == 0:
    prosta = 0
else:
    prosta = b/a
testy = int(input())
result = 0
for i in range(testy):
    x, y = [int(x) for x in input().split()]

    if x == 0 and prosta == 0 and y<b:
        result += 1
    elif x != 0 and y/x == prosta and x < a and y < b:
        result += 1
print(result)
