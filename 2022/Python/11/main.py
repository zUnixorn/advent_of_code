import part1
import part2

if __name__ == "__main__":
    with open("input") as file:
        lines = file.read()
    # lines = lines.split('\n\n')
    # lines = [block.split('\n')[1:] for block in lines]
    # for block in lines:
    #     items = [int(item) for item in block[0].split(": ")[-1].split(", ")]
    #     operation = eval("lambda old:" + block[1].split('=')[1])
    #     test = int(block[2].split(' ')[-1])
    #     true = int(block[3].split(' ')[-1])
    #     false = int(block[4].split(' ')[-1])
    #     print(test)
    #     print(true)
    #     print(false)
    print(part1.solution(lines))
    print(part2.solution(lines))
