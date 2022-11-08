import sys
def spacje(word: str):
    word1 = word.split()
    first = word1[0] # pobieramy pierwsze słowo
    word1 = [i.capitalize() for i in word1[1:]] # zwięszamy pierwsze litery

    word1.insert(0,first) # dodajemy na pierwsze miejsce
    word2 = ''.join(word1) # łączymy wszystko
    return word2


for line in sys.stdin: # wczytywanie linii
    print(spacje(line))
