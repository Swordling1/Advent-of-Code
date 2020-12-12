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

new = [0]
for i in range(length):
    if list[i] == num + 3:
        jolt3 += 1
        num = list[i]
    elif list[i] == num + 1:
        jolt1 += 1
        num = list[i]
    if num not in new: new.append(num)
jolt3 += 1
laptop = num + 3
print(jolt1 * jolt3)

ara = [0]
percent = 0
print(str(percent) + "%")
for x in range(length):
    if percent < round(x/length * 100):
        percent = round(x/length * 100)
        print(str(percent) + "%")
    for y in range(len(ara)):
        if ara[y] == num: continue
        j1 = ara[y] + 1 in list
        j2 = ara[y] + 2 in list
        j3 = ara[y] + 3 in list
        if j1 and j2 and j3:
            ara.append(ara[y] + 1)
            ara.append(ara[y] + 2)
            ara[y] += 3
        elif j1 and j3:
            ara.append(ara[y] + 1)
            ara[y] += 3
        elif j2 and j3:
            ara.append(ara[y] + 2)
            ara[y] += 3
        elif j1 and j2:
            ara.append(ara[y] + 1)
            ara[y] += 2
        else:
            if j1: ara[y] += 1
            if j2: ara[y] += 2
            if j3: ara[y] += 3
    print("current length: " + str(len(ara)))
print(len(ara))