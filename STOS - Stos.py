import sys

try:
    stack = []
    while True:
        dane = str(input())
        if dane != '':
            if dane == '+':
                if len(stack) < 10:
                    stack.insert(0,int(input()))
                    print(':)')
                else:
                    print(':(')
    
            elif dane == '-':
                if not stack:
                    print(':(')
                else:
                    print(stack[0])
                    stack.pop(0)
        else:
            break
            
except:
    sys.exit(0)
