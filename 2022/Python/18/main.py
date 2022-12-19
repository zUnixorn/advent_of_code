import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        voxels = [tuple(map(int, l[:-1].split(','))) for l in file.readlines()]
    print(part1.solution(voxels))
    print(part2.solution(voxels))