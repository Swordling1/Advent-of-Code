from pathlib import Path

#raw = Path('Day 7\input.txt').read_text()
raw = Path('Day 7\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

for i in range(length):
    raw[i] = raw[i].replace(".", "")
    raw[i] = raw[i].split(" contain ")
    if "no other" in raw[i][1]: raw[i][1] = "none"
    else: raw[i][1] = raw[i][1].split(", ")

bags = {}

for x in range(length):
    if raw[x][1] == "none": bags[raw[x][0]] = "none"
    else:
        num = []
        bag = []
        for y in range(len(raw[x][1])): num.append(raw[x][1][y][0])
        for y in range(len(raw[x][1])): bag.append(raw[x][1][y][2:])
        bags[raw[x][0]] = {}
        for y in range(len(raw[x][1])): bags[raw[x][0]][bag[y]] = num[y]

print(bb)