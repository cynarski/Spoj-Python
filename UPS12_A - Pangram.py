from collections import Counter

word = input()
lst = []
slownik = Counter(word)
if len(slownik) == 26:
    for i in slownik.values():
       if i not in lst:
            lst.append(i)
    if len(lst) == 1:
        print('PANGRAM PERFEKCYJNY')
    else:
        print('PANGRAM')

else:
    print('NIE')
