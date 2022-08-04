n = int(input())
word = list(input())
x = int((n-1)/2)
new_word = list(["."]*n)
for i in range(0,x+1):
    new_word[x-i] = word[x-i]
    new_word[x+i] = word[x+i]
    print(*new_word,sep='')