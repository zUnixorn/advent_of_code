from copy import deepcopy

import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = file.readlines()
        lines = [[ord(h) - 97 for h in l[:-1]] for l in lines]
    print(part1.solution(deepcopy(lines)))
    print(part2.solution(lines))
