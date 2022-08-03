testy = int(input())
max_zysk = 0
zysk = 0
for i in range(testy):
    x = int(input())
    if zysk + x < 0:
        zysk = 0
    else:
        zysk += x
        if(zysk>max_zysk):
            max_zysk = zysk
print(max_zysk)