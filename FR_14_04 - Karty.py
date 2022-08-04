def karty(arr):
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    result = 0
    for karty in arr:
        if karty in values:
            result += values[karty]
    return result


jas = input()
stas = input()
result1 = int(karty(jas))
result2= int(karty(stas))
if result1 == result2:
    print("REMIS")
elif result1 > result2:
    print("JASIO")
else:
    print("STASIO")