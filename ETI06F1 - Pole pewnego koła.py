dane = input().split(' ')
r = float(dane[0])
d = float(dane[1])
pi = 3.141592654
radius = (r ** 2 - (d/2)**2)**0.5
area = radius ** 2 * pi
print(round(area,2))
