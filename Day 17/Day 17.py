from pathlib import Path
import copy

#raw = Path('Day 17\input.txt').read_text()
raw = Path('Day 17\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

cube = [[]]

for i in range(length):
    cube[0].append([])
    for j in range(len(raw[i])): 
        if raw[i][j] == "#": cube[0][i].append(True)
        else: cube[0][i].append(False)

for i in range(1):
    length = len(cube[0]) + 2

print(bb)