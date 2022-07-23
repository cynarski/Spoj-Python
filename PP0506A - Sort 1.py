from operator import itemgetter
import math

testy = int(input())
for i in range(testy):
    p = int(input())
    points = []
    for j in range(p):
        points.append(list(map(str,input().split())))
        points[j].append(float(math.sqrt((int(points[j][1]))**2 + (int(points[j][2]))**2)))
    points = sorted(points, key = itemgetter(3))
    for k in range(len(points)):
        print(*points[k][0:3])
    if i != testy - 1:
        input()
        print()

# get_2 = itemgetter(2)
# s = 'abcdefghij'
# get_2(s) -> c
# myList = [10,20,30,40,50,60]
# get_2(myList) -> 30
# numbers = [4,2,12,8]
# print(sorted(numbers)) -> [2,4,8,12]




