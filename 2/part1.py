def score(left, right):
    score = right
    if left == right:
        score += 3
    elif (right - 1 - left + 1) % 3 == 1:
        score += 6
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

