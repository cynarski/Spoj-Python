a1, b1, c1, d1 = list(map(float,input().split()))
a2, b2, c2, d2 = list(map(int,input().split()))
w1 = (b1 * b2 + d1 * d2) / (b2+d2)
w2 = (a1 * a2 + c1 * c2) / (a2+c2)
w3 = (a1*a2 + b1*b2 + c1*c2 + d1*d2) / (a2 + b2 + c2 + d2)
print('K16K36: ','{:0.2f}'.format(w1))
print('M16M36: ','{:0.2f}'.format(w2))
print('M16K16M36K36: ','{:0.2f}'.format(w3))