from pathlib import Path

#raw = Path('Day 8\input.txt').read_text()
raw = Path('Day 8\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

for i in range(length):
    raw[i] = raw[i].split(" ")
    raw[i][1] = int(raw[i][1])
    raw[i].append(False)

print(bb)