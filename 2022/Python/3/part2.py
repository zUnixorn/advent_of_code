def priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

def duplicate(a, b, c):
    a, b, c = set(a), set(b), set(c)
    return a.intersection(b).intersection(c).pop()

def solution(lines):
    total = 0
    for i in range(0, len(lines), 3):
        total += priority(duplicate(lines[i][:-1], lines[i+1][:-1], lines[i+2][:-1]))
    return total