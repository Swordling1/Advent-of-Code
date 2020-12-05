from pathlib import Path

VALID = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
LENGTH = len(VALID)
EYE = ["amb","blu","brn","gry","grn","hzl","oth"]

raw = Path('Day 4\input.txt').read_text()
raw = raw.strip()
raw = raw.split("\n\n")

length = len(raw)

for i in range(length):
    raw[i] = raw[i].replace("\n", " ")

def valid_check(type, input, secondary = ""):
    if type == "byr":
        if int(input) >= 1920 and int(input) <= 2002: return(True)
    if type == "iyr":
        if int(input) >= 2010 and int(input) <= 2020: return(True)
    if type == "eyr":
        if int(input) >= 2020 and int(input) <= 2030: return(True)
    if type == "hgt" and secondary == "cm":
        if int(input) >= 150 and int(input) <= 193: return(True)
    elif type == "hgt" and secondary == "in":
        if int(input) >= 59 and int(input) <= 76: return(True)
    if type == "hcl":
        if "#" in input:
            input = input.replace("#", "")
            input = input.lower()
            if len(input) == 6:
                for i in range(6): 
                    if input[i] > "f": return(False)
                return(True)
    if type == "ecl":
        for i in range(len(EYE)):
            if EYE[i] in input: return(True)
    if type == "pid":
        if len(input) == 9 and input.isdigit(): return True
    if type == "cid": return(True)
    return(False)

valid = 0

for i in range(length):
    num = 0
    num2 = 0
    for o in range(LENGTH):
        if VALID[o] in raw[i]: num += 1
    if num == LENGTH: 
        raw[i] = raw[i].split(" ")
        length2 = len(raw[i])
        for x in range(len(raw[i])):
            type = ""
            raw[i][x] = raw[i][x].split(":")
            if "cm" in raw[i][x][1]: 
                type = "cm"
                raw[i][x][1] = raw[i][x][1].replace("cm", "")
            elif "in" in raw[i][x][1]:
                type = "in"
                raw[i][x][1] = raw[i][x][1].replace("in", "")
            if valid_check(raw[i][x][0], raw[i][x][1], type): num2 += 1
        if num2 == length2: valid += 1

print(valid)