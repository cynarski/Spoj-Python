from math import modf
testy = int(input())
secounds_during_run = 0
for i in range(testy):
    dane = list(map(str,input().split()))
    distance = int(dane[0])
    hours = str(dane[1][0:2])
    minutes = str(dane[1][3:5])
    secounds = str(dane[1][6:9])
    if hours[0] == '0':
        h = int(hours[1])
    elif hours[0] != 0:
        h = int(hours[0] + hours[1])
    if minutes[0] == '0':
        m = int(minutes[1])
    elif minutes[0] != 0:
        m = int(minutes[0] + minutes[1])
    if secounds[0] == '0':
        s = int(secounds[1])
    elif secounds[0] != 0:
        s = int(secounds[0] + secounds[1])
    secounds_during_run = h*3600 + m*60 + s
    secounds_afrer = secounds_during_run*1000/distance
    if modf(secounds_afrer)[0] >= 0.5:
        secounds_afrer += 1
    minutes_after = int(secounds_afrer/60)
    secounds_ = str(int(secounds_afrer) - 60*minutes_after)
    if len(secounds_) == 1:
        time = str(minutes_after) + ':' + '0' + secounds_
        print(time)
    else:
        time = str(minutes_after) + ':'  + secounds_
        print(time)