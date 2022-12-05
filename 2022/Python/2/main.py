import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = file.readlines()
    print(part1.solution(lines))
    print(part2.solution(lines))