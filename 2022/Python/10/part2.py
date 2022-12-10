def solution(lines):
    x = 1
    cycle = 1
    display = [['.' for _ in range(40)] for _ in range(6)]

    for op in lines:
        noop = op[0] == "noop"
        add = 0
        if noop:
            cycle_length = 1
        else:
            add = op[1]
            cycle_length = 2
        for _ in range(cycle_length):
            cursor_x = (cycle - 1) % 40
            if cursor_x > x - 2 and cursor_x < x + 2:
                display[(cycle - 1) // 40][cursor_x] = '#'
            # do something
            cycle += 1
        x += add

    return "\n".join(["".join(row) for row in display])
