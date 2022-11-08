kolory = {
    '#000000': 'black',
    '#C0C0C0': 'silver',
    '#808080': 'gray',
    '#FFFFFF': 'white',
    '#800000': 'maroon',
    '#FF0000': 'red',
    '#800080': 'purple',
    '#FF00FF': 'fuchsia',
    '#008000': 'green',
    '#00FF00': 'lime',
    '#808000': 'olive',
    '#FFFF00': 'yellow',
    '#000080': 'navy',
    '#0000FF': 'blue',
    '#008080': 'teal',
    '#00FFFF': 'aqua'


}
testy = int(input())
for i in range(testy):
    k1,k2,k3 = list(map(int,input().split()))
    liczba1 = str(hex(k1))[2:]
    liczba1 = liczba1.upper()
    liczba2 = str(hex(k2))[2:]
    liczba2 = liczba2.upper()
    liczba3 = str(hex(k3))[2:]
    liczba3 = liczba3.upper()
    if len(liczba1) == 1:
        liczba1 = '0' + liczba1
    if len(liczba2) == 1:
        liczba2 = '0' + liczba2
    if len(liczba3) == 1:
        liczba3 = '0' + liczba3
    kod = '#'+liczba1+liczba2+liczba3
    if kod in kolory:
        print(kolory[kod])
    else:
        print(kod)
