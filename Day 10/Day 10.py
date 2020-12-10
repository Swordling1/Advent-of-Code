from pathlib import Path
import copy

raw = Path('Day 10\input.txt').read_text()
#raw = Path('Day 10\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

list = []
for i in range(length): list.append(int(raw[i]))
list.sort()

num = 0
jolt1 = 0
jolt3 = 0

for i in range(length):
    if list[i] == num + 3:
        jolt3 += 1
        num = list[i]
    if list[i] == num + 1:
        jolt1 += 1
        num = list[i]
jolt3 += 1

print(num + 3)
print(jolt1)
print(jolt3)
print(jolt1 * jolt3)