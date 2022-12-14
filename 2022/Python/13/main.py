import part1
import part2
from ast import literal_eval

if __name__ == "__main__":
    with open("input") as file:
        lines = file.read()

    lines = lines.split('\n\n')
    lines = [[literal_eval(p) for p in l.split('\n')] for l in lines]
    print(part1.solution(lines))
    print(part2.solution(lines))
