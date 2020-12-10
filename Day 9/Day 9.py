from pathlib import Path
import copy

raw = Path('Day 9\input.txt').read_text()
#raw = Path('Day 9\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)
START = 25

list = []
for i in range(length): list.append(int(raw[i]))

invalid = 0
for i in range(START, length):
    o = i + 1
    num = list[i - START:i]
    valid = False
    for x in range(START):
        for y in range(START):
            if num[x] + num[y] == list[i]: valid = True
    if valid == False: invalid = list[i]

print(invalid)

for x in range(length):
    found = False
    num = []
    total = 0
    y = x
    while total <= invalid:
        if total < invalid:
            num.append(list[y])
            total += num[-1]
            y += 1
        if total == invalid:
            found = True
            break
    if found:
        num.sort()
        print(num[0] + num[-1])
        break