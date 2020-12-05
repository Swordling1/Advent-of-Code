from pathlib import Path
numbers = Path('Day 1\input.txt').read_text()
numbers = numbers.strip()
numbers = numbers.split("\n")
length = len(numbers)
for i in range(length): numbers[i] = int(numbers[i])
n1 = 0
n2 = 0
n3 = 0
equals = False
for i in range(length):
    for o in range(length):
        for x in range(length):
            if numbers[i] + numbers[o] + numbers[x] == 2020:
                n1 = numbers[i]
                n2 = numbers[o]
                n3 = numbers[x]
                equals = True
            if equals: break
        if equals: break
    if equals: break

print(n1 * n2 * n3)