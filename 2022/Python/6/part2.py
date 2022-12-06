def solution(line):
    for i in range(14, len(line) + 1):
        if len(set(line[i-14:i])) == 14:
            return i
