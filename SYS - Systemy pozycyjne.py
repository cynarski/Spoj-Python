def systemy_pozycyjne(a,b):
    system ={
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'

    }
    result = ""
    if a == 0:
        return '0'
    while a != 0:
        nowy = a % b
        result += system[int(nowy)]
        a = int(a/b)
    
    result = result[::-1]
    return result

testy = int(input())
for i in range(testy):
    a = int(input())
    print(systemy_pozycyjne(a,16),systemy_pozycyjne(a,11))
