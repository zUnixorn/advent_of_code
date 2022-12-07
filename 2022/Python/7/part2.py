from part1 import fs_tree

def solution(lines):
    root = fs_tree(lines).root()

    needed = 30000000 - 70000000 + root.size()

    for size in sorted(map(lambda x: x.size(), root.dirs_list())):
        if size >= needed:
            return size
