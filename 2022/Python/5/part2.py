from part1 import parameters

def solution(lines):
    lines = [l[:-1] for l in lines]
    crates = [[l[i] for l in reversed(lines[0:8]) if l[i] != ' '] for i in range(1, 34, 4)]
    moves = [parameters(m) for m in lines[10:]]

    for move in moves:
        crates[move[2]].extend(crates[move[1]][-move[0]:])
        crates[move[1]] = crates[move[1]][:-move[0]]

    return "".join([crates[i][-1] for i in range(9)])