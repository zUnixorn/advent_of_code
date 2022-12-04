def priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

def duplicate(items):
    half = len(items) // 2
    left = set(items[0:half])
    right = set(items[half:])

    return left.intersection(right).pop()

with open("rucksack") as file:
    lines = file.readlines()

total = 0
for line in lines:
    total += priority(duplicate(line[:-1]))

print(total)
