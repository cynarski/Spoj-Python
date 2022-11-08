import sys
def mors(arr):
    alfabet = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '.-..',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '..-.',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'R': '.-.',
        'Q': '--.-',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        ' ': ''
    }

    result = ''
    for mors in arr:
        if mors in alfabet:
            result += alfabet[mors] + '/'
    return result
try:
    while True:
        word = str(input())
        result = ''
        x = word.upper()
        for i in range(len(x)):
            result += x[i]
        print(mors(result))
except:
    sys.exit(0)
