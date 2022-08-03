testy = int(input())
for i in range(testy):
    inputs = list(map(int,input().split()))
    segments = inputs[0] - 1
    inputs.pop(0)
    legs = sum(inputs)
    print(segments+legs)