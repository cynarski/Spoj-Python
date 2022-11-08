dane = input().split(' ')
time = dane[2]
h_wsch= dane[0][:2]
min_wsch = dane[0][3:]
h_zach= dane[1][:2]
min_zach = dane[1][3:]
h_akt = dane[2][:2]
min_akt = dane[2][3:]

if int(h_wsch) < int(h_akt) < int(h_zach):
    print('dzien')
elif int(h_wsch) > int(h_akt) or int(h_zach) < int(h_akt):
    print('noc')
elif int(h_zach) == int(h_akt):
    if int(min_akt) == int(min_zach):
        print('noc')
    elif int(min_akt) > int(min_zach):
        print('noc')
    elif int(min_akt) < int(min_zach):
        print('dzien')
elif int(h_akt) == int(h_wsch):
    if int(min_akt) == int(min_wsch):
        print('dzien')
    elif int(min_akt) > int(min_wsch):
        print('dzien')
    elif int(min_akt) < int(min_wsch):
        print('noc')
