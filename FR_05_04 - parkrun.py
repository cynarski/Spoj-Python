best_time = 9999999999999
t = int(input())
for test in range(t):
    name = list(input().split())
    time = str(name[2])
    inttime = 0
    inttime += int(time[0:2]) * 60
    inttime += int(time[3:])
    if inttime == best_time:
        best_contestant.extend(name[:2])
    if inttime < best_time:
        best_time = inttime
        best_contestant = name[:2]
x = 0
while x < len(best_contestant):
    print(best_contestant[x], best_contestant[x+1])
    x += 2