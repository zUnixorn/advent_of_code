import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = file.readlines()[0][:-1]
    print(part1.solution(lines))
    print(part2.solution(lines))
