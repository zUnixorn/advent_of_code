from collections import defaultdict
from part1 import parse_lines

def hits(x, y, map):
    if y >= map["floor"]:
        return True

    for line in map.get(y, range(0, 0)):
        if x in line:
            return True
    
    return False

def solution(lines):
    map = parse_lines(lines)

    grains = 0
    
    map["floor"] = max(map.keys()) + 2

    while not map[0]:
        sx = 500
        sy = 0

        while True:
            sy += 1

            if not hits(sx, sy, map):
                continue
            
            if not hits(sx - 1, sy, map):
                sx -= 1
                continue
            
            if not hits(sx + 1, sy, map):
                sx += 1
                continue

            grains += 1
            map[sy - 1].append(range(sx, sx + 1))
            break
    
    return grains
