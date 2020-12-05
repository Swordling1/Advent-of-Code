from pathlib import Path

TREE = "#"
SLOPE = [[1,1],[3,1],[5,1],[7,1],[1,2]]

raw = Path('Day 3\input.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length_y = len(raw)
length_x = len(raw[0])

grid = []

for x in range(length_x): grid.append([])

for y in range(length_y):
    for x in range(length_x):
        grid[x].append(raw[y][x])
  
hits = []

for test in range(len(SLOPE)):
    x = 0
    hit = 0

    for y in range(0, length_y, SLOPE[test][1]):
        if grid[x][y] == TREE: hit +=1
        x += SLOPE[test][0]
        if x >= length_x: x -= length_x

    hits.append(hit)

final = 1
for i in range(len(hits)): final *= hits[i]

print(final)