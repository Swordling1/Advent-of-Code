from pathlib import Path
import copy

#raw = Path('Day 16\input.txt').read_text()
raw = Path('Day 16\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n\n")
LIST = type([])

fields, mine, nearby = raw[0].split("\n"), raw[1].split("\n")[1].split(","), raw[2].split("\n")[1:]
del raw

for i in range(len(fields)): 
    fields[i] = fields[i].split(": ")
    fields[i][1] = fields[i][1].split(" or ")
    for x in range(len(fields[i][1])): 
        fields[i][1][x] = fields[i][1][x].split("-")
        for y in range(len(fields[i][1][x])): fields[i][1][x][y] = int(fields[i][1][x][y])

for i in range(len(mine)): mine[i] = int(mine[i])

invalid = []

for i in range(len(nearby)): 
    nearby[i] = nearby[i].split(",")
    for x in range(len(nearby[i])): 
        nearby[i][x] = int(nearby[i][x])
        valid = False
        for y in range(len(fields)):
            if (nearby[i][x] >= fields[y][1][0][0] and nearby[i][x] <= fields[y][1][0][1]) or (nearby[i][x] >= fields[y][1][1][0] and nearby[i][x] <= fields[y][1][1][1]):
                valid = True
        if not valid: invalid.append(i)
for i in range(len(invalid)): nearby.pop(invalid[len(invalid) - 1 - i])
del invalid

placement = []

for x in range(len(fields)):
    place = []
    for y in range(len(mine)):
        if (mine[y] >= fields[x][1][0][0] and mine[y] <= fields[x][1][0][1]) or (mine[y] >= fields[x][1][1][0] and mine[y] <= fields[x][1][1][1]):
            place.append(y)
        for z in range(len(nearby)):
            if (nearby[z][y] >= fields[x][1][0][0] and nearby[z][y] <= fields[x][1][0][1]) or (nearby[z][y] >= fields[x][1][1][0] and nearby[z][y] <= fields[x][1][1][1]):
                place.append(y)
    place.sort()
    place_n, amount = [], []
    for i in range(len(place)):
        if place[i] not in place_n: 
            place_n.append(place[i])
            amount.append(1)
        else: 
            y = place_n.index(place[i])
            amount[y] += 1
    potential = []
    for i in range(len(place_n)):
        if amount[i] == len(nearby) + 1: potential.append(place_n[i])
    placement.append([fields[x][0]])
    if len(potential) > 1: placement[x].append(potential)
    else: placement[x].append(potential[0])
    del place, place_n, potential