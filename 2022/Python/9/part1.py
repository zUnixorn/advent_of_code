def solution(commands):
    x_head = 0
    y_head = 0

    x_tail = 0
    y_tail = 0

    opposite = {
        'R': 'L',
        'L': 'R',
        'U': 'D',
        'D': 'U'
    }

    visited = set()
    last_command = commands[0][0]
    jumped = False

    for command in commands:
        steps = command[1]
        # print(command)

        for _ in range(steps):
            # print(f"head: {x_head}, {y_head}")
            # print(f"tail: {x_tail}, {y_tail}")
            # print(f"command: {command[0]}")
            # print(f"last_command: {last_command}")


            if not jumped:
                # print("adding head")
                # visited.add((x_head, y_head))
                # last_command = command[0]
                # print()
                # print(f"tail: {x_tail}, {y_tail}")
                # print(f"head_last: {x_head_last}, {y_head_last}")
                # print("adding tail")
                printv(visited, (x_head, y_head), (x_tail, y_tail))
                visited.add((x_tail, y_tail))
            else:
                print("jumped")
                jumped = False

            print()

            if not (opposite[command[0]] == last_command):
                x_tail = x_head
                y_tail = y_head

            jumped = last_command in "RL" and command[0] in "UD" or last_command in "UD" and command[0] in "RL"
            last_command = command[0]
            # else:
            #     pass
                # visited.add((x_head, y_head))


            match command[0]:
                case 'R':
                    x_head += 1
                case 'L':
                    x_head -= 1
                case 'U':
                    y_head += 1
                case 'D':
                    y_head -= 1

            # print("adding tail")
            # print()
            # visited.add((x_tail, y_tail))
        
        last_command = command[0]
        # 4, 0 drin
    

    return len(visited)

def printv(visited, head, tail):
    for y in reversed(range(5)):
        for x in range(6):
            if (x, y) == head:
                print('H', end='')
            elif (x, y) == tail:
                print('T', end='')
            # elif (x, y) in visited:
            #     print('#', end='')
            else:
                print('.', end='')
        print()