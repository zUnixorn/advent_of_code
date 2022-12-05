def score(left, right):
    score = right
    if left == right:
        score += 3
    elif (right - 1 - left + 1) % 3 == 1:
        score += 6
    return score

def solution(lines):
    total = 0
    for line in lines:
        rps = line[0:-1].split(' ')
        total += score(ord(rps[0]) - 64, ord(rps[1]) - 87)
    return total