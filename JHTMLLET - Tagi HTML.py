import sys
def tagi_HTML(word: str):
    tag = False
    to_fix = list(map(str,word))
    for i in range(0, len(to_fix)):
        if(to_fix[i] == '<'):
            tag = True
        elif(to_fix[i] == '>'):
            tag = False
        if(tag):
            to_fix[i] = str(to_fix[i]).upper()
    result = ''.join(to_fix)
    return result



for line in sys.stdin:
    print(tagi_HTML(line))