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

bags = []
info = []

CLASS = type(bags)

for x in range(length):
    bags.append(raw[x][0])
    if type(raw[x][1]) == CLASS: 
        info.append(raw[x][1])
        for y in range(len(info[x])): info[x][y] = [int(info[x][y][0]), info[x][y][2:]]
    else: info.append("none")

needed = ["shiny gold bags"]
count = 0

while len(needed) > 0:
    new = []
    for i in range(len(needed)):
        need = bags.index(needed[i])
        if type(info[need]) == CLASS:
            for x in range(len(info[need])):
                for y in range(info[need][x][0]): 
                    new.append(info[need][x][1])
                    count +=1
        else: count +=1
    needed = new
print(count)