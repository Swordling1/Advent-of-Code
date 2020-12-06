from pathlib import Path

raw = Path('Day 6\input.txt').read_text()
raw = raw.strip()
raw = raw.split("\n\n")

length = len(raw)

for i in range(length):
    raw[i] = raw[i].replace("\n", "")

print(bb)
