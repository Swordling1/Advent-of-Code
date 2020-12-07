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

for i in range(length):
    if raw[i][1] == "none": bags[raw[i][0]] = "none"
    else: 
        bags[raw[i][0]] = {}
print(bb)