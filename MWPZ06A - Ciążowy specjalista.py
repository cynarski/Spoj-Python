testy = int(input())
for i in range(testy):
    inputs = list(map(int, input().split()))
    print(round(abs(12 * ((inputs[0] + inputs[1]) - (inputs[1] * inputs[2])) / (inputs[2] - 1))))