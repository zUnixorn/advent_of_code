def solution(lines):
    trees = [list(line) for line in lines]

    y_len = len(trees)
    x_len = len(trees[0])

    total = x_len * 2 + y_len * 2 - 4

    for y in range(1, y_len - 1):
        for x in range(1, x_len - 1):
            height = trees[y][x]
            cross = [
                trees[y][:x], 
                trees[y][x+1:], 
                [trees[r][x] for r in range(y)], 
                [trees[r][x] for r in range(y+1, y_len)]
            ]

            total += int(any(map(lambda t: visible(height, t), cross)))

    return total

def visible(height, trees):
    return all(map(lambda t: t < height, trees))
