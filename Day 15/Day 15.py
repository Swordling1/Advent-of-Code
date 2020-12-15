from pathlib import Path
import copy

raw = Path('Day 15\input.txt').read_text()
#raw = Path('Day 15\\test.txt').read_text()
raw = raw.strip()
raw = raw.split(",")

length = len(raw)

memory = []
for i in range(length): memory.append(int(raw[i]))

COUNT = 30000000

percent = 0
print(str(percent) + "%")

for x in range(length, COUNT):
    if round(x/COUNT * 100) != percent: 
        percent = round(x/COUNT * 100)
        print(str(percent) + "%")
    last = memory[-1]
    if memory.index(last) == len(memory)-1:
        memory.append(0)
    else: 
        for y in range(len(memory)):
            i = len(memory) - y - 2
            if memory[i] == memory[-1]: 
                memory.append(y+1)
                break
print(memory[-1])