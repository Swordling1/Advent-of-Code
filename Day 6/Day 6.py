from pathlib import Path

raw = Path('Day 6\input.txt').read_text()
raw = raw.strip()
raw = raw.split("\n\n")

length = len(raw)

for i in range(length):
    raw[i] = raw[i].replace("\n", "")


count = 0

for x in range(length):
    c = ""
    for y in range(len(raw[x])):
        if raw[x][y] not in c: c = c + raw[x][y]
    count += len(c)

print(count)
