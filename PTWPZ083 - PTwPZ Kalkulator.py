testy = int(input())
for t in range(testy):
    dane = input()
    result = int(dane[0])
    for i in range(len(dane)):
        if dane[i] == "+":
            result += int(dane[i+1])
        if dane[i] == "-":
            result -= int(dane[i+1])
    print(result)