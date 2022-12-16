import re

import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = [list(map(lambda x: tuple(map(int, x)), re.findall("x=(-?\d+), y=(-?\d+)", l))) for l in file.readlines()]
    print(part1.solution(lines))
    print(part2.solution(lines))