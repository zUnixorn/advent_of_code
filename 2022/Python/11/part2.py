from collections import defaultdict
from functools import reduce

# from https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
def gcde(a, b):
    if a == 0:
        return b,0,1

    gcd,x1,y1 = gcde(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y

# from https://youtu.be/ZoACsszuhAE
def solve_congruence_system(results, ms):
    ms_product = reduce(lambda a, b: a * b, ms, 1)
    upper_ms = [ms_product // m for m in ms]

    return sum([gcde(m, um)[2] * um * r for (m, um, r) in zip(ms, upper_ms, results)])


class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = lambda x: true if x % test == 0 else false
        self.inspections = 0

    def inspect_all(self):
        receivers = defaultdict(list)
        self.inspections += len(self.items)

        for item in self.items:
            item = self.operation(item)

            results = [item % m for m in self.mods]
            item = solve_congruence_system(results, self.mods)
                
            # Include for solution
            # item = item // 3

            receiver = self.test(item)
            receivers[receiver].append(item)

        self.items.clear()
        return receivers

def parse_monkeys(lines):
    lines = lines.split('\n\n')
    lines = [block.split('\n')[1:] for block in lines]
    monkeys = []
    mods = []
    for block in lines:
        items = [int(item) for item in block[0]. split(": ")[-1].split(", ")]
        operation = eval("lambda old:" + block[1].split('=')[1])
        test = int(block[2].split(' ')[-1])
        true = int(block[3].split(' ')[-1])
        false = int(block[4].split(' ')[-1])
        monkeys.append(Monkey(items, operation, test, true, false))
        mods.append(test)
    
    for monkey in monkeys:
        monkey.mods = mods

    return monkeys

        

def solution(lines):
    monkeys = parse_monkeys(lines)
    for _ in range(10000):
        for monkey in monkeys:
            receivers = monkey.inspect_all()

            for receiver in receivers.keys():
                monkeys[receiver].items += receivers[receiver]
    
    inspections = list(sorted((m.inspections for m in monkeys)))

    return inspections[-2] * inspections[-1]
