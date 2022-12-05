def parameters(op):
    parameters = [0, 0, 0]
    op = op[5:]
    op = op.split(" from ")
    parameters[0] = int(op[0])
    op = op[1].split(" to ")
    parameters[1] = op[0]
    parameters[2] = op[1]
    return (parameters[0], parameters[1], parameters[2])

with open("crates") as file:
    lines = file.readlines()

lines = [l[:-1] for l in lines]

# TODO parse crates to 2d array
crates = lines[0:8]
moves = [parameters(m) for m in lines[10:]]

print(crates)
print("--------")
print(moves)
