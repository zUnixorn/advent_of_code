def solution(pairs):
    max_xy = 4_000_000

    for y in range(max_xy + 1):
        occupied = []

        for [(sx, sy), (bx, by)] in pairs:
            offset_x = abs(sx - bx) + abs(sy - by) - abs(sy - y)
            
            if offset_x <= 0:
                continue

            occupied.append((max(sx - offset_x, 0), min(sx + offset_x, max_xy)))
        
        occupied.sort(key=lambda x: x[0])
        
        if occupied[0][0] > 0:
            break

        i = 1

        while i < len(occupied):
            first = occupied[i - 1]
            second = occupied[i]

            if first[0] <= second[0] and first[1] >= second[1]:
                occupied.pop(i)
                continue
            

            if first[1] < second[0] - 1:
                break

            i += 1
        else:
            if occupied[-1][1] < max_xy:
                break
            continue
        
        break
    else:
        return "no uncovered spot found"

    return (occupied[i][0] - 1) * max_xy + y