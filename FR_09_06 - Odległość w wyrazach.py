testy = int(input())
for _ in range(testy):
    lst = []
    word = input()
    for i in word:
        lst.append(ord(i))

    lst.sort()
    print(lst[-1] - lst[0])