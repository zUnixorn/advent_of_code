import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = [l[:-1].split(' ') for l in file.readlines()]
        lines = [[l[0], int(l[1])] for l in lines]
    print(part1.solution(lines))
    print(part2.solution(lines))
