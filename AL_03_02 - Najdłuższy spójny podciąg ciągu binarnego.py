tab = [0] * 500002
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    q = input()
    index = 0
    jed = 0
    pom = 0
    mx = 0
    s = 0

    for i in range(n):
        if q[i] == '0':
            pom += 1
        elif jed < k:
            jed += 1
            pom += 1
            tab[s] = i
            s += 1
        else:
            if pom > mx:
                mx = pom
            pom = i - tab[index]
            index += 1
            tab[s] = i
            s += 1
    if pom > mx:
        mx = pom
    print(mx)