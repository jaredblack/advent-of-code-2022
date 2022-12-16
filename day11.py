in_file = open('in/day11.txt')
st = in_file.read()
in_file.close()

class Monkey:
    def __init__(self, items, op, test, true_dest, false_dest, div_n):
        self.items = items
        self.op = op
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspection_count = 0
        self.div_n = div_n

class FactorizedItem:
    def __init__(self, item, factors):
        self.item = item
        self.factors = factors

monkeys = []
important_factors = []
for monkey in st.split('\n\n'):
    lines = monkey.splitlines()
    items = list(map(int, lines[1].split(': ')[1].split(', ')))
    operator = lines[2].split(': ')[1].split('old ')[1][0]
    operand = lines[2].split(': ')[1].split(operator + ' ')[1]
    if operator == '+':
        op = lambda x, operand=operand: x + int(operand)
    else:
        if operand == 'old':
            op = lambda x: x * x
        else: 
            op = lambda x, operand=operand: x * int(operand)
    
    div_n = int(lines[3].split('by ')[1])
    important_factors.append(div_n)
    test = lambda x, div_n = div_n: x % div_n == 0
    true_dest = int(lines[4].split('monkey ')[1])
    false_dest = int(lines[5].split('monkey ')[1])
    monkeys.append(Monkey(items, op, test, true_dest, false_dest, div_n))

for _ in range(20):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            monkey.inspection_count += 1
            item = monkey.op(item)
            item //= 3
            if monkey.test(item):
                monkeys[monkey.true_dest].items.append(item)
            else:
                monkeys[monkey.false_dest].items.append(item)
        monkey.items = []


counts = sorted([x.inspection_count for x in monkeys])
print(counts[-1] * counts[-2])

# reset monkeys
# Part 2
megafactor = 1
for monkey in monkeys:
    megafactor *= monkey.div_n
    

for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            monkey.inspection_count += 1
            item = monkey.op(item)
            item %= megafactor
            if monkey.test(item):
                monkeys[monkey.true_dest].items.append(item)
            else:
                monkeys[monkey.false_dest].items.append(item)
        monkey.items = []


counts = sorted([x.inspection_count for x in monkeys])
print(counts[-1] * counts[-2])