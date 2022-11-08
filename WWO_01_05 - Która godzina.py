h1, h2, m1, m2 = [str(x) for x in input().split()]
result = str(int(h1,2)) + str(int(h2,2)) + ':' + str(int(m1,2)) + str(int(m2,2))
print(result)