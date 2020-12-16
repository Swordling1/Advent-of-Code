from pathlib import Path
import copy

#raw = Path('Day 16\input.txt').read_text()
raw = Path('Day 16\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n\n")

fields, mine, nearby = raw[0].split("\n"), raw[1].split("\n")[1].split(","), raw[2].split("\n")[1:]

for i in range(len(fields)): 
    fields[i] = fields[i].split(": ")
    fields[i][1] = fields[i][1].split(" or ")
    for x in range(len(fields[i][1])): fields[i][1][x] = fields[i][1][x].split("-")

for i in range(len(mine)): mine[i] = int(mine[i])

for i in range(len(nearby)): 
    nearby[i] = nearby[i].split(",")
    for x in range(len(nearby[i])): nearby[i][x] = int(nearby[i][x])
