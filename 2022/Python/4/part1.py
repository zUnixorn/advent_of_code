def contained(a1, a2, b1, b2):
    return b1 <= a1 and b2 >= a2 or a1 <= b1 and a2 >= b2

def solution(lines):
    total = 0
    for line in lines:
        line = line[:-1].split(',')
        a = [int(i) for i in line[0].split('-')]
        b = [int(i) for i in line[1].split('-')]
        if contained(a[0], a[1], b[0], b[1]):
            total += 1
    return total