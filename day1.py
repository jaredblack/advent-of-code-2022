in_file = open('in/day1.txt')
st = in_file.read()
in_file.close()

l = [[int(y) for y in x.split('\n')] for x in st.split('\n\n')]

l2 = max([sum(n) for n in l])
print(f"Part 1: {l2}")

l3 = sorted([sum(n) for n in l])
print(f"Part 2: {sum(l3[-3:])}")
