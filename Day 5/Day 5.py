from pathlib import Path

raw = Path('Day 5\input.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

row = []
column = []

for i in range(length):
    row.append(raw[i][:7])
    column.append(raw[i][7:])

highest_id = 0
ids = []

for x in range(length):
    r = 0
    for y in range(len(row[x])):
        if row[x][y] == "B": r += 2**(len(row[x])-y-1)
    c = 0
    for y in range(len(column[x])):
        if column[x][y] == "R": c += 2**(len(column[x])-y-1)
    id = r * 8 + c
    ids.append(id)
    if id > highest_id:
        highest_id = id

ids.sort()
id = ids[0]
for i in range(len(ids)):
    if id < ids[i]-1:
        id = ids[i]-1
        break
    else:
        id = ids[i]

print(highest_id)
print(id)