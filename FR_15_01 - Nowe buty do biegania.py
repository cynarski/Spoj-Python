def km_to_mile(x: int):
    return x/1.609344

n = int(input())
if km_to_mile(n) < 300:
    print("NIE")
elif 300 <= km_to_mile(n) < 500:
    print("SPRAWDZIMY TWOJE OBECNE BUTY")
elif km_to_mile(n) >= 500:
    print("TAK")