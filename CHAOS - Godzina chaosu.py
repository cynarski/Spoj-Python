import sys


def palindr(integer):
    return int(str(integer)[::-1])


def time_print(hour, minute):
    if hour < 10 and minute < 10:
        print(f"0{hour}:0{minute}")
    elif hour < 10:
        print(f"0{hour}:{minute}")
    elif minute < 10:
        print(f"{hour}:0{minute}")
    else:
        print(f"{hour}:{minute}")


try:
    tests = int(input())
    for t in range(tests):
        h, m = map(int, input().split(':'))
        if h == 0:
            if m < 10:
                if m == 9:
                    time_print(0, 11)
                else:
                    m += 1
                    time_print(h, m)
            else:
                if m == palindr(m) or m != palindr(m):
                    if m >= 55:
                        time_print(1, 1)
                    else:
                        m += 1
                        while m != palindr(m):
                            m += 1
                        time_print(h, m)
                else:
                    while m != palindr(m):
                        m += 1
                    time_print(h, m)

        elif h == 16 or h == 17 or h == 18 or h == 19:
            time_print(20, 2)

        elif h < 10:
            if h == 9 and m > 48:
                if m == 59:
                    time_print(10, 1)
                    continue
                else:
                    time_print(9, 59)
                    continue
            m += 1
            while True:
                if m >= 59:
                    h += 1
                    m = 0
                whole = int(str(h) + str(m))
                if whole == palindr(whole):
                    break
                m += 1
            time_print(h, m)

        else:
            if h == 23 and m >= 32:
                time_print(0, 0)
            elif h == 15 and m >= 51:
                time_print(20, 2)
            elif m < palindr(h):
                time_print(h, palindr(h))
            else:
                h += 1
                time_print(h, palindr(h))
except:
    sys.exit(0)