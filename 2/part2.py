def score(left, right):
    score = right * 3 - 3
    if right == 1:
        score += (left - 1 + 2) % 3 + 1
    elif right == 3:
        score += (left - 1 + 1) % 3 + 1
    else:
        score += left
    return score
    # print(f"{left} {right}")

with open("rps") as file:
    lines = file.readlines()

total = 0
for line in lines:
    rps = line[0:-1].split(' ')
    # print(rps[0])
    total += score(ord(rps[0]) - 64, ord(rps[1]) - 87)
print(total)

