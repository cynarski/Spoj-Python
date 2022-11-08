from math import sqrt, pow

dane = list(map(int, input().split()))
ax = dane[0]
ay = dane[1]
bx = dane[2]
by = dane[3]
cx = dane[4]
cy = dane[5]

ab = sqrt(pow(ax - bx, 2) + pow(ay - by, 2))
ac = sqrt(pow(ax - cx, 2) + pow(ay - cy, 2))
bc = sqrt(pow(bx - cx, 2) + pow(by - cy, 2))
p = (ab + bc + ac) / 2
pole = sqrt(p * (p - ab) * (p - bc) * (p - ac))
r = ab * bc * ac / (4 * pole)

print('{:0.2f}'.format(r))