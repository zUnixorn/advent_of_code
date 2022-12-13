import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = file.read()

    lines = lines.split('\n\n')
    lines = [[eval(p) for p in l.split('\n')] for l in lines]
    print(part1.solution(lines))
    print(part2.solution(lines))
