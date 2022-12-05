from collections import defaultdict
import re
import copy

in_file = open('in/day5.txt')
st = in_file.read()
in_file.close()

def create_stax(st):
    stax = defaultdict(lambda: [])
    for line in st.splitlines():
        col = 1
        for i in range(1, len(line), 4):
            if line[i].isalpha():
                stax[col].append(line[i])
            elif line[i].isnumeric():
                return stax
            col += 1

stax = create_stax(st)
for stak in stax:
    stax[stak].reverse()
orig_stax = copy.deepcopy(stax)

start = st.index("move")
st = st[start:]
for cmd in st.splitlines():
    num, start_stack, end_stack = [int(s) for s in re.findall(r'\b\d+\b', cmd)]
    for i in range(num):
        popped = stax[start_stack].pop()
        stax[end_stack].append(popped)

for i in range(1, len(stax) + 1):
    print(stax[i][-1], end='')
print()

# Part 2
stax = orig_stax
for cmd in st.splitlines():
    num, start_stack, end_stack = [int(s) for s in re.findall(r'\b\d+\b', cmd)]
    popped = stax[start_stack][-num:]
    stax[start_stack] = stax[start_stack][:-num]
    stax[end_stack] += popped

for i in range(1, len(stax) + 1):
    print(stax[i][-1], end='')
print()
