in_file = open('in/day4.txt')
st = in_file.read()
in_file.close()

num = 0

for pair in st.split('\n'):
    elf1, elf2 = pair.split(',')
    time1, time2 = map(int, elf1.split('-'))
    time3, time4 = map(int, elf2.split('-'))
    if (time1 >= time3 and time2 <= time4) \
     or time3 >= time1 and time4 <= time2:
     num += 1

print(f"Part 1: {num}")     

num = 0
for pair in st.split('\n'):
    elf1, elf2 = pair.split(',')
    time1, time2 = map(int, elf1.split('-'))
    time3, time4 = map(int, elf2.split('-'))
    r1 = set(range(time1, time2 + 1))
    r2 = set(range(time3, time4 + 1))
    intersec = r1.intersection(r2)
    if len(intersec):
        num += 1

print(f"Part 2: {num}")     
