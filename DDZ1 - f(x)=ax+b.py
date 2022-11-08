a,b = list(map(int,input().split()))
a1 = str(a)
b1 = str(b)
if a == 0:
    print('f(x)='+b1)
elif a != 0 and a != 1 and a != -1 and b > 0:
    print('f(x)='+a1+'x+'+b1)
elif a != 0 and a != 1 and a != -1 and b == 0:
    print('f(x)='+a1+'x')
elif a != 0 and a != 1 and a != -1 and b < 0:
    print('f(x)='+a1+'x'+b1)
elif a == 1 and b == 0:
    print('f(x)='+'x')
elif a == 1 and b > 0:
    print('f(x)='+'x'+'+'+ b1)
elif a == 1 and b < 0:
    print('f(x)='+'x'+ b1)
elif a == -1 and b == 0:
    print('f(x)='+'-x')
elif a == -1 and b > 0:
    print('f(x)='+'-x'+'+'+ b1)
elif a == -1 and b < 0:
    print('f(x)='+'-x'+ b1)
