niedowaga= []
norma = []
nadwaga = []
def bmi(name:str,a:float,b:float):
    b = b/100
    bmi = a/(b*b)
    if bmi < 18.5:
        niedowaga.append(name)
        return
    elif 18.5 <= bmi < 25:
        norma.append(name)
        return
    elif bmi >= 25:
        nadwaga.append(name)
        return
testy = int(input())
for i in range(testy):
    dane = input().split(' ')
    name = str(dane[0])
    weight = float(dane[1])
    height = float(dane[2])
    bmi(name,weight,height)
print('niedowaga')
for i in range(len(niedowaga)):
    print(niedowaga[i])
print()
print('wartosc prawidlowa')
for i in range(len(norma)):
    print(norma[i])
print()
print('nadwaga')
for i in range(len(nadwaga)):
    print(nadwaga[i])