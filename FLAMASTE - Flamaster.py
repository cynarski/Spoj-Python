def flamaster(word):
    word += '0' # nwm czemu to potrzebne ale nie działa poprawnie bez tego
    letter = ''
    ile = 1
    result = ""
    for i in word:
        if i == letter:
            ile += 1
        else:
            if ile > 2:
                result += letter + str(ile)
            elif ile == 2:
                result += letter * 2
            else:
                result += letter
            ile = 1
        letter = i
    return result



testy = int(input())
for i in range(testy):
    dane = input()
    print(flamaster(dane))
