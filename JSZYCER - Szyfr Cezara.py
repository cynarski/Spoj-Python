import sys
try:
    while True:
        inputs = list(map(str,input()))
        if inputs != '':
            for i in range(len(inputs)):
                if inputs[i] == ' ' or inputs[i] == '\n':
                    continue
                elif inputs[i] =='X' or inputs[i] == 'Y' or inputs[i] == 'Z':
                    inputs[i] = chr(ord(inputs[i])-23)
                else:
                    inputs[i] = chr(ord(inputs[i]) + 3)

            inputs= ''.join(inputs)
            print(inputs)
            inputs=''
        else:
            break
except:
    sys.exit(0)