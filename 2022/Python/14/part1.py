from collections import defaultdict

def parse_lines(lines):
    # could be optimized by removing intersection duplicates
    map = defaultdict(list)

    for line in lines:
        for i in range(1, len(line)):
            a = [int(a) for a in line[i - 1].split(',')]
            b = [int(a) for a in line[i].split(',')]


            begin = min(a[0],  b[0])

            # vertical
            if a[0] == b[0]:
                for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                    map[y].append(range(begin, begin + 1))
            else:
                map[a[1]].append(range(begin, max(a[0], b[0]) + 1))
    
    return map

# could be optimized by checking all 3 locations at the same time
def hits(x, y, map):
    for line in map.get(y, range(0, 0)):
        if x in line:
            return True
    
    return False

def solution(lines):
    map = parse_lines(lines)

    grains = 0
    done = False

    while not done:
        sx = 500
        sy = 0

        while True:
            if sy > max(map.keys()):
                done = True
                break

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
