from functools import reduce

def solution(lines):
    trees = [list(line) for line in lines]

    y_len = len(trees)
    x_len = len(trees[0])

    max = 0

    for y in range(1, y_len - 1):
        for x in range(1, x_len - 1):
            height = trees[y][x]
            cross = [
                list(reversed(trees[y][:x])), 
                trees[y][x+1:], 
                [trees[r][x] for r in reversed(range(y))], 
                [trees[r][x] for r in range(y+1, y_len)]
            ]

            score = reduce(lambda a, t: a * visible(height, t), cross, 1)
            if score > max:
                max = score 

    return max

def visible(height, trees):
    return next((i for i in range(len(trees)) if trees[i] >= height), len(trees) - 1) + 1
