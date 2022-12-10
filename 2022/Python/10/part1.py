def solution(lines):
    x = 1
    cycle = 1
    interesting_cycle = 20
    result = []

    for op in lines:
        noop = op[0] == "noop"
        add = 0
        if noop:
            cycle_length = 1
        else:
            add = op[1]
            cycle_length = 2
        for _ in range(cycle_length):
            if cycle == interesting_cycle:
                result.append(x * cycle)
                interesting_cycle += 40
            cycle += 1
        x += add

    return sum(result)
