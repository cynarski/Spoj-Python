n = int(input())
letters= list(map(str,input().split()))
word = str(input())
result = ''
for i in range(len(word)):
    if word[i] in letters:
        result += word[i]*2
    else:
        result += word[i]
print(result)