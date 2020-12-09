from pathlib import Path

raw = Path('Day 8\input.txt').read_text()
#raw = Path('Day 8\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

for i in range(length):
    raw[i] = raw[i].split(" ")
    raw[i][1] = int(raw[i][1])
    raw[i].append(False)

acc = 0
i = 0

while True:
    if raw[i][2]: break
    if raw[i][0] == "nop": 
        raw[i][2] = True
        i += 1
    elif raw[i][0] == "acc":
        acc += raw[i][1]
        raw[i][2] = True
        i += 1
    elif raw[i][0] == "jmp":
        raw[i][2] = True
        i += raw[i][1]

print(acc)