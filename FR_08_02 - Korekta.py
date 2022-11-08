testy = int(input())
for i in range(testy):
    w1, l1, w2, l2, w3, l3 = [int(x) for x in input().split()]
    wins = w1 + w2 + w3
    loses = l1 + l2 + l3
    matchesPlayed = (w1 + l1)*4
    print((matchesPlayed//2) -wins, (matchesPlayed//2) - loses)