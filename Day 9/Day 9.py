from pathlib import Path
import copy

raw = Path('Day 9\input.txt').read_text()
#raw = Path('Day 9\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)
start = 25

list = []
for i in range(length): list.append(int(raw[i]))

invalid = 0
for i in range(start, length):
    o = i + 1
    num = list[i - start:i]
    valid = False
    for x in range(start):
        for y in range(start):
            if num[x] + num[y] == list[i]: valid = True
    if valid == False: invalid = list[i]

print(invalid)