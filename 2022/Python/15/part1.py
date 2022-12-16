def solution(pairs):
    y = 2000000
    xs = set()

    for [(sx, sy), (bx, by)] in pairs:
        offset_x = abs(sx - bx) + abs(sy - by) - abs(sy - y)

        for x in range(-offset_x, offset_x + 1):
            xs.add(sx + x)
        
        if by == y:
            xs.remove(bx)

    return len(xs)