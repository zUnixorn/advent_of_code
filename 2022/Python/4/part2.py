def overlaps(a1, a2, b1, b2):
    return a2 >= b1 and b2 >= a1

def solution(lines):
    total = 0
    for line in lines:
        line = line[:-1].split(',')
        a = [int(i) for i in line[0].split('-')]
        b = [int(i) for i in line[1].split('-')]
        if overlaps(a[0], a[1], b[0], b[1]):
            total += 1
    return total