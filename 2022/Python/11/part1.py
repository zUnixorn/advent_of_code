from collections import defaultdict

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
            item = item // 3

            receiver = self.test(item)
            receivers[receiver].append(item)

        self.items.clear()
        return receivers

def parse_monkeys(lines):
    lines = lines.split('\n\n')
    lines = [block.split('\n')[1:] for block in lines]
    monkeys = []
    for block in lines:
        items = [int(item) for item in block[0]. split(": ")[-1].split(", ")]
        operation = eval("lambda old:" + block[1].split('=')[1])
        test = int(block[2].split(' ')[-1])
        true = int(block[3].split(' ')[-1])
        false = int(block[4].split(' ')[-1])
        monkeys.append(Monkey(items, operation, test, true, false))

    return monkeys

        

def solution(lines):
    monkeys = parse_monkeys(lines)
    for _ in range(20):
        for monkey in monkeys:
            receivers = monkey.inspect_all()

            for receiver in receivers.keys():
                monkeys[receiver].items += receivers[receiver]
    
    inspections = list(sorted((m.inspections for m in monkeys)))

    return inspections[-2] * inspections[-1]
