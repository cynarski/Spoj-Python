word = str(input())
result = ''
for i in range(0,len(word),2):
    result += word[i]
if len(word) % 2:
    back = 2
else:
    back = 1
for i in range(len(word) - back,0,-2):
    result += word[i]

print(result)