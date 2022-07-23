def StringMerge(word1, word2):
    newword = ""
    if len(word1) < len(word2):
        length = len(word1)
    else:
        length = len(word2)

    for i in range(length):
        newword += word1[i] + word2[i]
    return newword


testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    print(StringMerge(dane[0],dane[1]))

