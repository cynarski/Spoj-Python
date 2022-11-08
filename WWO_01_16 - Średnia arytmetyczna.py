from statistics import mean
input()
dane = [int(x) for x in input().split()]
srednia = mean(dane)
dane.sort(key=lambda x: abs(x-srednia))
print(dane[0])