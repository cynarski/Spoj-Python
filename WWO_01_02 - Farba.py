from math import ceil

a,b,c = list(map(int,input().split()))
pole_sufitu = a*b
pole_scian = 2*a*c + 2*b*c
puszki_na_sufit = ceil(pole_sufitu/3)
puszki_na_sciane = ceil(pole_scian/5)
print(puszki_na_sciane + puszki_na_sufit)

