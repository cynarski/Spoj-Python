import sys

points = 0
s1 = sys.stdin.readline()
s2 = sys.stdin.readline()
s3 = sys.stdin.readline()

for i in range(len(s1)):

    if s1[i] != s2[i] or s1[i] != s3[i]:
        if s2[i] == s3[i]:
            points += 2
        else:
            points += 1
print(points)