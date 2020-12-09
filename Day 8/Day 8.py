from pathlib import Path
import copy

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
flag = []

while True:
    if raw[i][2]: break
    if raw[i][0] == "nop": 
        raw[i][2] = True
        if raw[i][1] != 0: flag.append(i)
        i += 1
    elif raw[i][0] == "acc":
        acc += raw[i][1]
        raw[i][2] = True
        i += 1
    elif raw[i][0] == "jmp":
        raw[i][2] = True
        i += raw[i][1]

print(acc)

for i in range(length):
    raw[i][2] = False

acc = []
for x in range(length):
    special = copy.deepcopy(raw)
    worked = True
    acc_l = 0
    i = 0

    for o in range(length):
        special[o][2] = False
    
    if special[x][0] == "nop": special[x][0] = "jmp"
    elif special[x][0] == "jmp": special[x][0] = "nop"

    while worked:
        if special[i][2]: 
            worked = False
        if special[i][0] == "nop": 
            special[i][2] = True
            i += 1
        elif special[i][0] == "acc":
            acc_l += special[i][1]
            special[i][2] = True
            i += 1
        elif special[i][0] == "jmp":
            special[i][2] = True
            i += special[i][1]
        if i >= length:
            break
    if worked:
        acc.append(acc_l)


print(acc)