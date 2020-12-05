from pathlib import Path

raw = Path('Day 2\input.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)

for i in range(length): raw[i] = raw[i].split(":")
for i in range(length): raw[i][1] = raw[i][1].strip()

raw2 = []
for i in range(length): raw2.append(raw[i][0].split(" "))

passwords = []
for i in range(length): passwords.append(raw[i][1])

letter = []
for i in range(length): letter.append(raw2[i][1])

amount = []
for i in range(length): amount.append(raw2[i][0].split("-"))
for i in range(length):
    amount[i][0] = int(amount[i][0])
    amount[i][1] = int(amount[i][1])

valid = 0
part = input("What part would you like? ")

def debug(num):
    print(passwords[num])
    print(letter[num])
    print(amount[num])
"""
x = 0
passwords[x] = "x0ff"
letter[x] = "x"
amount[x] = [1, 4]
"""

if part == "1":
    for x in range(length):
        #debug(x)
        i = passwords[x].count(letter[x])
        if i >= amount[x][0] and i <= amount[x][1]: 
            # print("VALID!!!")
            valid += 1
        #else: print("NOT VALID!!")

elif part == "2":
    for x in range(length):
        #debug(x)

        i = passwords[x][amount[x][0] - 1]
        o = passwords[x][amount[x][1] - 1]
        
        if (i == letter[x]) ^ (o == letter[x]): 
            valid += 1
            #print("VALID!!")
        #print("\n")

print(valid)