from pathlib import Path

raw = Path('Day 6\input.txt').read_text()
raw = raw.strip()
raw = raw.split("\n\n")

length = len(raw)

part_1 = []

for i in range(length): part_1.append(raw[i].replace("\n", ""))


count = 0

for x in range(length):
    c = ""
    for y in range(len(part_1[x])):
        if part_1[x][y] not in c: c = c + part_1[x][y]
    count += len(c)

print(count)

count = 0
part_2 = []

for i in range(length): part_2.append(raw[i].split("\n"))

for x in range(length):
    c = []
    for y in range(len(part_2[x][0])):
        if part_2[x][0][y] not in c: c.append(part_2[x][0][y])
    for y in range(len(part_2[x])):
        for i in range(len(c)):
            if c[i] not in part_2[x][y]: 
                m = True
                c[i] = " "
    count += len(c) - c.count(" ")
print(count)