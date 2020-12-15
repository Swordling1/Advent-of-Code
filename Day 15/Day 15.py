from pathlib import Path
import copy

#raw = Path('Day 15\input.txt').read_text()
raw = Path('Day 15\\test.txt').read_text()
raw = raw.strip()
raw = raw.split(",")

length = len(raw)

memory = []
for i in range(length): memory.append(int(raw[i]))

for i in range(length, 2020):
    print(aaa)