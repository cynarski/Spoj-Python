import fileinput


def foo(n,i):
    next_number = n - 9*10**(i-1)*i
    if next_number <= 0:
        return n//i
    return 9*10**(i-1) + foo(next_number,i+1)


with fileinput.input() as f:
    for number in f:
        number = int(number)
        print(foo(number,1))