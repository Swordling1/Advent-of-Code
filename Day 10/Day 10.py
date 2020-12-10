from pathlib import Path
import copy

raw = Path('Day 10\input.txt').read_text()
#raw = Path('Day 10\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

list = []
for i in range(length): list.append(int(raw[i]))

