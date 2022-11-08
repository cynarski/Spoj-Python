stopnie_hours = 360/12
stopnie_minutes =360/60
testy = int(input())
for i in range(testy):
    godzina = str(input())
    for j in range(len(godzina)):
        if godzina[j] == ':':
            hours = int(godzina[:j])
            minutes = int(godzina[j+1:])
    stopnie = stopnie_hours * hours + stopnie_hours * (minutes/60) - stopnie_minutes*minutes

    while stopnie >= 360:
        stopnie -= 360
    while stopnie < 0:
        stopnie += 360
    if stopnie > 180:
        stopnie = 360 -stopnie

    print(stopnie)