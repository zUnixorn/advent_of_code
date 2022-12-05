def parameters(op):
    parameters = [0, 0, 0]
    op = op[5:]
    op = op.split(" from ")
    parameters[0] = int(op[0])
    op = op[1].split(" to ")
    parameters[1] = int(op[0]) - 1
    parameters[2] = int(op[1]) - 1
    #      (count,         source,        destination  )
    return (parameters[0], parameters[1], parameters[2])

with open("crates") as file:
    lines = file.readlines()

lines = [l[:-1] for l in lines]
crates = [[l[i] for l in reversed(lines[0:8]) if l[i] != ' '] for i in range(1, 34, 4)]
moves = [parameters(m) for m in lines[10:]]

for move in moves:
    crates[move[2]].extend(crates[move[1]][-move[0]:])
    crates[move[1]] = crates[move[1]][:-move[0]]

print("".join([crates[i][-1] for i in range(9)]))